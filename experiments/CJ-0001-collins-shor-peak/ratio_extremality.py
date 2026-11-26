"""Test of the ratio-extremality hypothesis (Conjecture A of the CJ-0001 investigation).

For a tree T of order n write rho_k(T) = d_{k+1}(T) / d_k(T), 0 <= k <= n-3,
S_n for the star and P_n for the path. The hypothesis is

  (i)  rho_k(T) >= rho_k(S_n)   for 0 <= k <= floor(n/2) - 1,
  (ii) rho_k(T) <= rho_k(P_n)   for 0 <= k <= min(p_n, n-3),
       p_n = largest maximizing index of P_n (rho_k is defined for k <= n-3;
       when p_n = n-2 the upper bound on the peak is vacuous).

Together with log-concavity, (i) at k = floor(n/2) - 1 and (ii) at k = p_n give
peak(S_n) <= peak(T) <= peak(P_n), hence the Collins–Shor interval whenever the
star and the path satisfy it. Hypothesis (i) is refuted at order 20; see
research/active/CJ-0001-collins-shor-peak/STATE.md.

Ratios are compared by integer cross-multiplication (exact). Two modes:

  exhaustive  every tree of each order;
  sampled     pseudo-random trees of larger orders from several models, with a
              recorded seed (evidence only for the trees actually sampled).

Usage:
    python experiments/CJ-0001-collins-shor-peak/ratio_extremality.py exhaustive --min-order 4 --max-order 18 --out <file>
    python experiments/CJ-0001-collins-shor-peak/ratio_extremality.py sampled --orders 30 40 60 --samples 2000 --seed 20261126 --out <file>
"""

from __future__ import annotations

import argparse
import json
import multiprocessing
import random
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import distpoly  # noqa: E402

CHUNK = 2000
_reference: dict[int, tuple[list[int], list[int], int]] = {}


def reference(n: int) -> tuple[list[int], list[int], int]:
    """(star sequence, path sequence, largest maximizing index of the path)."""
    if n not in _reference:
        star = distpoly.scaled_coefficients(distpoly.star_parents(n))
        path = distpoly.scaled_coefficients(distpoly.path_parents(n))
        _reference[n] = (star, path, distpoly.peak_indices(path)[-1])
    return _reference[n]


def analyse(parents: list[int]) -> dict:
    """Exact comparison of one tree with the star and the path."""
    n = len(parents)
    star, path, path_peak = reference(n)
    sequence = distpoly.scaled_coefficients(parents)
    # star_ok[k]: rho_k(T) >= rho_k(S_n);  path_ok[k]: rho_k(T) <= rho_k(P_n).
    star_ok = [sequence[k + 1] * star[k] >= star[k + 1] * sequence[k] for k in range(n - 2)]
    path_ok = [sequence[k + 1] * path[k] <= path[k + 1] * sequence[k] for k in range(n - 2)]
    low, high = distpoly.conjectured_interval(n)
    peaks = distpoly.peak_indices(sequence)
    return {
        "star_ok": star_ok,
        "path_ok": path_ok,
        "violates_i": not all(star_ok[: n // 2]),
        "violates_ii": not all(path_ok[: min(path_peak, n - 3) + 1]),
        "violates_collins_shor": peaks[0] < low or peaks[-1] > high,
    }


def process_chunk(chunk: list[bytes]) -> dict:
    n = len(chunk[0])
    star_all = [True] * (n - 2)
    path_all = [True] * (n - 2)
    bad_i, bad_ii, bad_cs = [], [], []
    for raw in chunk:
        layout = list(raw)
        result = analyse(distpoly.parents_from_layout(layout))
        star_all = [a and b for a, b in zip(star_all, result["star_ok"])]
        path_all = [a and b for a, b in zip(path_all, result["path_ok"])]
        if result["violates_i"]:
            bad_i.append(layout)
        if result["violates_ii"]:
            bad_ii.append(layout)
        if result["violates_collins_shor"]:
            bad_cs.append(layout)
    return {"count": len(chunk), "star_all": star_all, "path_all": path_all, "bad_i": bad_i, "bad_ii": bad_ii, "bad_cs": bad_cs}


def chunked(iterable):
    batch: list[bytes] = []
    for layout in iterable:
        batch.append(bytes(layout))
        if len(batch) == CHUNK:
            yield batch
            batch = []
    if batch:
        yield batch


def summarise(n: int, results) -> dict:
    started = time.monotonic()
    star_all = [True] * (n - 2)
    path_all = [True] * (n - 2)
    count, bad_i, bad_ii, bad_cs = 0, [], [], []
    for result in results:
        count += result["count"]
        star_all = [a and b for a, b in zip(star_all, result["star_all"])]
        path_all = [a and b for a, b in zip(path_all, result["path_all"])]
        bad_i.extend(result["bad_i"])
        bad_ii.extend(result["bad_ii"])
        bad_cs.extend(result["bad_cs"])
    _, _, path_peak = reference(n)
    return {
        "order": n,
        "trees": count,
        "path_peak": path_peak,
        "range_i": [0, n // 2 - 1],
        "range_ii": [0, min(path_peak, n - 3)],
        "violations_i": len(bad_i),
        "violations_ii": len(bad_ii),
        "violations_collins_shor": len(bad_cs),
        "violating_layouts_i": bad_i[:20],
        "violating_layouts_ii": bad_ii[:20],
        # Index sets on which the star (resp. path) is extremal among all trees examined.
        "indices_where_star_minimises_rho": [k for k, ok in enumerate(star_all) if ok],
        "indices_where_path_maximises_rho": [k for k, ok in enumerate(path_all) if ok],
        "seconds": round(time.monotonic() - started, 1),
    }


# ----------------------------------------------------------------- sampling --


def random_layout_models(n: int, rng: random.Random):
    """Yield (model name, parent array) for one tree from each random model."""
    # Uniform random labelled tree via a random Prüfer sequence, re-rooted to a parent array.
    prufer = [rng.randrange(n) for _ in range(n - 2)]
    degree = [1] * n
    for v in prufer:
        degree[v] += 1
    edges = []
    leaves = sorted(v for v in range(n) if degree[v] == 1)
    import heapq

    heapq.heapify(leaves)
    for v in prufer:
        leaf = heapq.heappop(leaves)
        edges.append((leaf, v))
        degree[v] -= 1
        if degree[v] == 1:
            heapq.heappush(leaves, v)
    edges.append((heapq.heappop(leaves), heapq.heappop(leaves)))
    yield "uniform-labelled", parents_from_edges(n, edges)
    # Random recursive tree: vertex i attaches to a uniform earlier vertex.
    yield "recursive", [-1] + [rng.randrange(i) for i in range(1, n)]
    # Random caterpillar: a spine of random length with the other vertices hung on random spine vertices.
    spine = rng.randrange(2, n)
    yield "caterpillar", [-1] + list(range(spine - 1)) + [rng.randrange(spine) for _ in range(n - spine)]
    # Random spider: legs of random lengths attached to a centre.
    parents, remaining = [-1], n - 1
    while remaining:
        leg = rng.randrange(1, remaining + 1)
        previous = 0
        for _ in range(leg):
            parents.append(previous)
            previous = len(parents) - 1
        remaining -= leg
    yield "spider", parents
    # Preferential-attachment-like tree: attach to an endpoint of a uniform random existing edge.
    parents = [-1, 0]
    endpoints = [0, 1]
    for vertex in range(2, n):
        target = rng.choice(endpoints)
        parents.append(target)
        endpoints += [target, vertex]
    yield "preferential", parents


def parents_from_edges(n: int, edges: list[tuple[int, int]]) -> list[int]:
    """Relabel a tree in breadth-first order from vertex 0 so that parent[i] < i."""
    adjacency = [[] for _ in range(n)]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    order, new_label, parents = [0], {0: 0}, [-1]
    for vertex in order:
        for neighbour in adjacency[vertex]:
            if neighbour not in new_label:
                new_label[neighbour] = len(order)
                order.append(neighbour)
                parents.append(new_label[vertex])
    return parents


def run_sampled(orders: list[int], samples: int, seed: int) -> list[dict]:
    rng = random.Random(seed)
    output = []
    for n in orders:
        started = time.monotonic()
        per_model: dict[str, dict] = {}
        for _ in range(samples):
            for model, parents in random_layout_models(n, rng):
                stats = per_model.setdefault(model, {"trees": 0, "violations_i": 0, "violations_ii": 0, "violations_collins_shor": 0, "examples": []})
                result = analyse(parents)
                stats["trees"] += 1
                for key in ("violates_i", "violates_ii", "violates_collins_shor"):
                    if result[key]:
                        stats[key.replace("violates", "violations")] += 1
                        if len(stats["examples"]) < 5:
                            stats["examples"].append({"kind": key, "parents": parents})
        _, _, path_peak = reference(n)
        output.append({"order": n, "path_peak": path_peak, "conjectured_interval": list(distpoly.conjectured_interval(n)),
                       "models": per_model, "seconds": round(time.monotonic() - started, 1)})
        print(f"n={n}: " + "; ".join(f"{m}: {s['trees']} trees, (i) {s['violations_i']}, (ii) {s['violations_ii']}, C-S {s['violations_collins_shor']}" for m, s in per_model.items()), flush=True)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    modes = parser.add_subparsers(dest="mode", required=True)
    exhaustive = modes.add_parser("exhaustive")
    exhaustive.add_argument("--min-order", type=int, default=4)
    exhaustive.add_argument("--max-order", type=int, required=True)
    exhaustive.add_argument("--workers", type=int, default=1)
    exhaustive.add_argument("--out", type=Path)
    sampled = modes.add_parser("sampled")
    sampled.add_argument("--orders", type=int, nargs="+", required=True)
    sampled.add_argument("--samples", type=int, default=1000)
    sampled.add_argument("--seed", type=int, required=True)
    sampled.add_argument("--out", type=Path)
    args = parser.parse_args()

    report: dict = {"experiment": "CJ-0001 ratio extremality (Hypotheses A(i) and A(ii))", "mode": args.mode,
                    "arithmetic": "exact integers", "run": distpoly.run_metadata()}
    if args.mode == "exhaustive":
        pool = multiprocessing.Pool(args.workers) if args.workers > 1 else None
        report["orders"] = []
        try:
            for n in range(args.min_order, args.max_order + 1):
                source = chunked(distpoly.layouts(n))
                results = pool.imap_unordered(process_chunk, source) if pool else map(process_chunk, source)
                entry = summarise(n, results)
                report["orders"].append(entry)
                print(f"n={n:>2} trees={entry['trees']:>8} (i) violations={entry['violations_i']} (ii) violations={entry['violations_ii']} "
                      f"C-S violations={entry['violations_collins_shor']} star-min on k={entry['indices_where_star_minimises_rho']} "
                      f"path-max on k={entry['indices_where_path_maximises_rho']}", flush=True)
        finally:
            if pool:
                pool.close()
                pool.join()
    else:
        report["seed"] = args.seed
        report["samples_per_model_per_order"] = args.samples
        report["orders"] = run_sampled(args.orders, args.samples, args.seed)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, indent=1) + "\n", encoding="utf-8", newline="\n")
        print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
