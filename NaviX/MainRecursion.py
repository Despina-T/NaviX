import Basics
import Splits
import Boom

side = 'START'
l_A, l_B = 0, 0  # lengths of the left segments of each sequence after splitting
s_d = []
''' In this 2D list, every element contains the depth of the recursion that the match was found and the letter
    'R' or 'L' that shows if the much is found on the right or on the left side of the previous match.
    Only in the first pair instead of letter has the word 'START'. It is parallel list with the one that 
    contains the indexes of the matches.'''


'''The function of the main recursion!!!! It starts with the initial match, and call itself 2 times
one for left segments and one for right'''
def div_and_conq(seq1, seq2, coors, TARGET_L, depth=0):
    global side, l_B, l_A, s_d
    length = TARGET_L
    booms, res = Boom.fun(seq1, seq2, length)
    '''increase the length of target seqs if no match is found only for this certain iteration'''
    while res is False and length <= len(seq1) and length <= len(seq2):
        length = length + 1
        if length <= len(seq1) and length <= len(seq2):
            booms, res = Boom.fun(seq1, seq2, length)
    if res:
        if depth == 0:
            side = 'START'
            coors.append(booms)
            l_A, l_B = booms[0], booms[1]
            s_d.append([depth, side])
        else:
            '''In this part the indexes of the match get fixed using the s_d list. Different calculation takes place
            based in the side that the current match is found in comparison with the one with depth-1.'''
            s_d.append([depth, side])
            x = coors[Basics.previous_depth(s_d, len(s_d))]
            if side == 'R':
                coors.append([booms[0] + x[0] + 1, booms[1] + x[1] + 1])
            elif side == 'L':
                coors.append([booms[0] + x[0] - l_A, booms[1] + x[1] - l_B])
        new_seq1, new_seq2, new_seq3, new_seq4= Splits.splits(seq1, seq2, booms)
        if len(new_seq1) >= TARGET_L and len(new_seq2) >= TARGET_L:
            '''After the splitting into new sequences call the next recursion only if both of the left segments are
            greater or equal to the Target-length'''
            l_A, l_B = len(new_seq1), len(new_seq2)
            side = 'L'
            div_and_conq(new_seq1, new_seq2, coors, TARGET_L, depth + 1)
        if len(new_seq3) >= TARGET_L and len(new_seq4) >= TARGET_L:
            '''After the splitting into new sequences call the next recursion only if both of the right segments are
            greater or equal to the Target-length'''
            side = 'R'
            div_and_conq(new_seq3, new_seq4, coors, TARGET_L, depth + 1)
    return coors
