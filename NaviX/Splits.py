# Take the indexes of a match and returns left part of the 2 seqs
def split_left(seq1, seq2, lst):
    left1 = seq1[: lst[0]]
    left2 = seq2[: lst[1]]
    return left1, left2


# Take the indexes of a match and returns right part of the 2 seqs
def split_right(seq1, seq2, lst):
    right1 = seq1[lst[0] + 1:]
    right2 = seq2[lst[1] + 1:]
    return right1, right2


# Combines the two splits-more useful for recursion
def splits(seq1, seq2, b):
    length1, length2 = len(seq1), len(seq2)
    seq_a1, seq_a2, seq_b1, seq_b2 = '', '', '', ''
    if length1 > 1 and length2 > 1:
        seq_a1, seq_b1 = split_left(seq1, seq2, b)
        seq_a2, seq_b2 = split_right(seq1, seq2, b)
    return seq_a1, seq_b1, seq_a2, seq_b2
