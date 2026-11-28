from fractions import Fraction as F
from itertools import product, combinations
from box_search import C1_pi, volume
for den in (2, 3, 4, 5, 6, 8, 10):
    pts = [F(k, den) for k in range(den + 1)]
    ivs = list(combinations(pts, 2))
    found = []
    for (a1, b1), (a2, b2), (a3, b3) in product(ivs, repeat=3):
        v = volume(C1_pi, [a1, a2, a3], [b1, b2, b3])
        if v < 0:
            found.append((v, (a1, b1), (a2, b2), (a3, b3)))
    if found:
        found.sort()
        v, *box = found[0]
        print("den", den, "negative boxes:", len(found), "most negative:", v, [tuple(map(str, b)) for b in box])
        # also a 'simplest' one: smallest sum of endpoints' denominators
        break
    else:
        print("den", den, "no negative box")
