"""CJ-0001, objective O7: what the failures of statement (S) found by
slope_family.py mean for (E'') and for (E). Exact integer arithmetic.

Notation of slope_family.py and notes/gamma-components.md. By the slope
identity (2c) of slope_family.py, S(T, nu, u, v) is the increment of
F(T + w', nu, u) when the weight n of a new leaf w' attached at v goes up by 1.
So a failure of (S) on a tree with j vertices suggests a failure of (E'') on a
tree with j + 1 vertices for some weight n. This script does not use that
identity: it computes every polynomial below directly from its definition.

For each failure of (S) stored in the result file of slope_family.py (the
examples and the smallest failure), with data (T, nu, u, v), j vertices:

(a) T+ = T with a new leaf w' = j attached at v, weight n. For n = 0, 1, ...,
    --max-n the script computes F(T+, (nu, n), u) and stops at the first n for
    which it is not in C_{j+3}: a failure of (E'') on j + 1 vertices
    (nu != 0 there). It also records whether
    F(T+, (nu, n), u) - F(T+, (nu, n-1), u) = S(T, nu, u, v) at that n.

(b) T++ = T+ with a second new leaf w = j + 1 attached at u. Statement (E)
    for (T++, w) reads: if every leaf of T++ has weight >= 1, then
    E = R(T++, nu0 + e_w) - R(T++, nu0) is in C_{j+3}, where nu0 has weight 0
    at w and R(T, nu) = (N + j - 1)(1+x) Phi - p^T adj(M) p (the definition).
    The leaves of T++ are w', w and the leaves of T other than u and v, so the
    hypothesis is: n >= 1 and nu >= 1 on those leaves of T. When it holds, the
    script computes E for every n = 1..--max-n, counts the n for which E is not
    in C_{j+3}, records E at the n found in (a) (at n = 1 if (a) found none or
    found n = 0), and checks E = x R(T+, (nu, n) + e_u) + F(T+, (nu, n), u)
    there (the relation between (E) and (E'') stated in STATE.md).

(c) For each failure (T', nu, u) of (E'') stored in the result file itself:
    T = T' with a new leaf w attached at u; if every leaf of T' other than u
    has weight >= 1 (the hypothesis of (E) for T), E for (T, w), whether it is
    in C_{j'+2}, and the relation E = x R(T', nu + e_u) + F(T', nu, u).

Finite exact checks. A failure in (a) is a counterexample to (E'') as stated
in STATE.md, to be confirmed by slope_family_verify.py; "no failure" in (b) is
a statement about the listed instances and weights only.

Command:

    uv run python experiments/CJ-0001-collins-shor-peak/slope_family_extension.py --max-n 200 --out experiments/CJ-0001-collins-shor-peak/results/slope-family-extension.json
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import networkx as nx

import slope_family as sf

HERE = Path(__file__).resolve().parent


def adjacency(edges, j):
    nbrs = {v: [] for v in range(j)}
    for a, b in edges:
        nbrs[a].append(b)
        nbrs[b].append(a)
    return nbrs


def R_value(edges, nu):
    """R(T, nu) = (N + j - 1)(1 + x) Phi(T, nu) - p^T adj(M(T, nu)) p."""
    j = len(nu)
    nbrs = adjacency(edges, j)
    phi, adj, _ = sf.weighted_data(nbrs, tuple(range(j)), tuple(nu))
    p = [[1, 2 - len(nbrs[v]) - nu[v]] for v in range(j)]
    quad = []
    for a in range(j):
        for b in range(j):
            quad = sf.padd(quad, sf.pmul(sf.pmul(p[a], p[b]), adj[a][b]))
    total = sum(nu) + j - 1
    return sf.ptrim(sf.padd(sf.pmul([total, total], phi), sf.pscale(quad, -1)))


def E_value(edges, nu, w):
    """E = R(T, nu0 + e_w) - R(T, nu0), nu0 = nu with weight 0 at w."""
    low = list(nu)
    low[w] = 0
    high = list(low)
    high[w] = 1
    return sf.ptrim(sf.padd(R_value(edges, high), sf.pscale(R_value(edges, low), -1)))


def extend(failure, max_n):
    j, edges, nu, u, v = failure["order"], failure["edges"], failure["nu"], failure["u"], failure["v"]
    out = dict(S_failure=dict(order=j, edges=edges, nu=nu, u=u, v=v))
    edges1 = edges + [[v, j]]
    # (a)
    found = None
    cases = 0
    for n in range(max_n + 1):
        cases += 1
        F = sf.F_value(edges1, nu + [n], u)
        if not sf.hg_ok(F, j + 3):
            found = n
            break
    out["E2_scan"] = dict(n_from=0, n_to=max_n, cases=cases, first_failure_n=found)
    out["E2_failure"] = None
    out["difference_equals_S"] = None
    if found is not None:
        out["E2_failure"] = dict(order=j + 1, edges=edges1, nu=nu + [found], u=u, F=F,
                                 half_gamma=sf.half_gamma(F, j + 3))
        if found >= 1:
            previous = sf.F_value(edges1, nu + [found - 1], u)
            out["difference_equals_S"] = sf.peq(sf.padd(F, sf.pscale(previous, -1)), failure["S"])
    # (b)
    nbrs = adjacency(edges, j)
    hypothesis = all(nu[x] >= 1 for x in range(j) if len(nbrs[x]) == 1 and x not in (u, v))
    out["E_hypotheses_hold"] = hypothesis
    out["E_scan"] = None
    out["E_value"] = None
    out["E_equals_xR_plus_F"] = None
    if hypothesis:
        edges2 = edges1 + [[u, j + 1]]
        w = j + 1
        at = found if found else 1
        failures = 0
        first = None
        for n in range(1, max_n + 1):
            E = E_value(edges2, nu + [n, 1], w)
            ok = sf.hg_ok(E, j + 3)
            if not ok:
                failures += 1
                if first is None:
                    first = n
            if n == at:
                out["E_value"] = dict(order=j + 2, edges=edges2, nu=nu + [n, 1], w=w, E=E, in_cone=ok,
                                      half_gamma=sf.half_gamma(E, j + 3))
                raised = nu + [n]
                raised[u] += 1
                rhs = sf.padd([0] + R_value(edges1, raised), sf.F_value(edges1, nu + [n], u))
                out["E_equals_xR_plus_F"] = sf.peq(E, rhs)
        out["E_scan"] = dict(n_from=1, n_to=max_n, cases=max_n, failures=failures, first_failure_n=first)
    return out


def e_at_e2_failure(failure):
    """(c) For a stored failure (T', nu, u) of (E''): E for T = T' with a new leaf w attached at u."""
    j, edges, nu, u = failure["order"], failure["edges"], failure["nu"], failure["u"]
    nbrs = adjacency(edges, j)
    hypothesis = all(nu[x] >= 1 for x in range(j) if len(nbrs[x]) == 1 and x != u)
    out = dict(E2_failure=dict(order=j, edges=edges, nu=nu, u=u), E_hypotheses_hold=hypothesis,
               E_value=None, E_equals_xR_plus_F=None)
    if hypothesis:
        edges1 = edges + [[u, j]]
        E = E_value(edges1, nu + [1], j)
        out["E_value"] = dict(order=j + 1, edges=edges1, nu=nu + [1], w=j, E=E, in_cone=sf.hg_ok(E, j + 2),
                              half_gamma=sf.half_gamma(E, j + 2))
        raised = list(nu)
        raised[u] += 1
        out["E_equals_xR_plus_F"] = sf.peq(E, sf.padd([0] + R_value(edges, raised), sf.F_value(edges, nu, u)))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--result", default=str(HERE / "results" / "slope-family.json"))
    ap.add_argument("--max-n", type=int, default=200)
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv)
    start = time.time()
    with open(args.result, encoding="utf-8") as fh:
        result = json.load(fh)
    failures = list(result["S"]["failure_examples"])
    smallest = result["S"].get("smallest_failure")
    if smallest is not None and smallest not in failures:
        failures.append(smallest)
    instances = [extend(failure, args.max_n) for failure in failures]
    e2_failures = list(result["E2"]["failure_examples"])
    smallest = result["E2"].get("smallest_failure")
    if smallest is not None and smallest not in e2_failures:
        e2_failures.append(smallest)
    stored = [e_at_e2_failure(failure) for failure in e2_failures]
    res = dict(
        instances=instances,
        E_at_stored_E2_failures=stored,
        summary=dict(
            stored_E2_failures=len(stored),
            stored_E2_failures_with_E_hypotheses=sum(1 for i in stored if i["E_value"] is not None),
            stored_E2_failures_with_E_not_in_cone=sum(
                1 for i in stored if i["E_value"] is not None and not i["E_value"]["in_cone"]),
            S_failures_extended=len(instances),
            E2_failures_found=sum(1 for i in instances if i["E2_failure"] is not None),
            least_n_of_an_E2_failure=min((i["E2_scan"]["first_failure_n"] for i in instances
                                          if i["E2_failure"] is not None), default=None),
            E_instances=sum(1 for i in instances if i["E_scan"] is not None),
            E_cases=sum(i["E_scan"]["cases"] for i in instances if i["E_scan"] is not None),
            E_failures=sum(i["E_scan"]["failures"] for i in instances if i["E_scan"] is not None),
        ),
        provenance=dict(
            command=" ".join(sys.argv if argv is None else ["slope_family_extension.py", *argv]),
            revision=sf.git("rev-parse", "HEAD"), dirty_tree=bool(sf.git("status", "--porcelain")),
            python=sys.version.split()[0], networkx=nx.__version__,
            seconds=round(time.time() - start, 1), arguments=vars(args),
        ),
    )
    text = json.dumps(res, indent=1)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
