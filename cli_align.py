#!/usr/bin/env python3
"""CLI for computing global alignment score (Needleman-Wunsch).

Usage:
  python cli_align.py SEQ1 SEQ2 [--match 1 --mismatch -1 --gap -1]

Outputs the global alignment score and (optionally) one optimal alignment.
"""
import argparse
from typing import Tuple, List


def global_alignment(seq1: str, seq2: str, match: int = 1, mismatch: int = -1, gap: int = -1) -> Tuple[int, Tuple[str, str]]:
    n = len(seq1)
    m = len(seq2)
    # DP matrix
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] + gap
    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] + gap

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            score_diag = dp[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch)
            score_up = dp[i - 1][j] + gap
            score_left = dp[i][j - 1] + gap
            dp[i][j] = max(score_diag, score_up, score_left)

    # Traceback to produce one alignment
    i, j = n, m
    aln1: List[str] = []
    aln2: List[str] = []
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            score_here = dp[i][j]
            score_diag = dp[i - 1][j - 1]
            opt_diag = score_diag + (match if seq1[i - 1] == seq2[j - 1] else mismatch)
            if score_here == opt_diag:
                aln1.append(seq1[i - 1])
                aln2.append(seq2[j - 1])
                i -= 1
                j -= 1
                continue
        if i > 0 and dp[i][j] == dp[i - 1][j] + gap:
            aln1.append(seq1[i - 1])
            aln2.append('-')
            i -= 1
            continue
        if j > 0 and dp[i][j] == dp[i][j - 1] + gap:
            aln1.append('-')
            aln2.append(seq2[j - 1])
            j -= 1
            continue
        # fallback (should not happen)
        break

    alignment = ("".join(reversed(aln1)), "".join(reversed(aln2)))
    return dp[n][m], alignment


def main():
    parser = argparse.ArgumentParser(description="Compute global alignment score for two sequences")
    parser.add_argument("seq1", help="First sequence")
    parser.add_argument("seq2", help="Second sequence")
    parser.add_argument("--match", type=int, default=1, help="Match score (default 1)")
    parser.add_argument("--mismatch", type=int, default=-1, help="Mismatch score (default -1)")
    parser.add_argument("--gap", type=int, default=-1, help="Gap penalty (default -1)")
    parser.add_argument("--show-alignment", action="store_true", help="Show one optimal alignment")
    args = parser.parse_args()

    score, (a1, a2) = global_alignment(args.seq1, args.seq2, args.match, args.mismatch, args.gap)
    print(f"Global alignment score: {score}")
    if args.show_alignment:
        print("Alignment:")
        print(a1)
        print(a2)


if __name__ == "__main__":
    main()
