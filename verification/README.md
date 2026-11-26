# Verification receipts

`receipts/` contains the machine-written output of `scripts/verify_lean.py`.
Each file name carries the UTC time, the Git commit that was verified, `-dirty`
if the working tree had uncommitted changes, and the verdict.

Receipts are never edited by hand. What a receipt does and does not establish
is defined in [`docs/verification-policy.md`](../docs/verification-policy.md).
