import Basics
import random


# Selects the l-search middle nucleotides of each seq. If there are not enough it takes different cases
# This one works better for the score in small sequences, but in big needs  significantly more time that target-seq2
def target_seq(seq1, seq2, length):
    if len(seq1) >= length and len(seq2) >= length:
        return Basics.o_e(seq1, len(seq1), length), Basics.o_e(seq2, len(seq2), length)
    elif len(seq2) >= length:
        if length > len(seq1) > 0:
            return seq1, Basics.o_e(seq2, len(seq2), length)
        else:
            return '', ''
    elif len(seq1) >= length:
        if length > len(seq2) > 0:
            return Basics.o_e(seq1, len(seq1), length), seq2
        else:
            return '', ''
    else:
        return seq1, seq2


# Selects the l-search middle nucleotides of each seq and returns an empty strings if l_search is bigger than one
# of the sequences
def target_seq2(seq1, seq2, length):
    if len(seq1) >= length and len(seq2) >= length:
        return Basics.o_e(seq1, len(seq1), length), Basics.o_e(seq2, len(seq2), length)
    else:
        return '', ''


# Discover random matches in the selected areas of the initial sequences
def boom(tseq1, tseq2, seq1, seq2, length):
    i = 0
    b1, b2 = len(tseq1) // 2, len(tseq2) // 2
    # if match won't be found after l1+l2 iteration, stops
    while not Basics.match(tseq1[b1], tseq2[b2]) and i < len(tseq1) + len(tseq2):
        b1, b2 = random.randint(0, len(tseq1) - 1), random.randint(0, len(tseq2) - 1)
        i += 1
    if Basics.match(tseq1[b1], tseq2[b2]):
        b1_1, b2_2 = Basics.fix_coors(b1, seq1, tseq1, length), Basics.fix_coors(b2, seq2, tseq2, length)
        return [b1_1, b2_2], Basics.match(tseq1[b1], tseq2[b2])
    else:
        return [], Basics.match(tseq1[b1], tseq2[b2])


# Used to combine previous functions
def fun(seq1, seq2, length):
    test_seq1, test_seq2 = target_seq2(seq1, seq2, length)
    bb,  b = boom(test_seq1, test_seq2, seq1, seq2, length)
    return bb, b
