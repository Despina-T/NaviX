# When a sequence is entered by the user confirms that it is a DNA sequence
# If it is not, requests a new one
def validation():
    seq = input()
    seq = seq.upper()
    count = 0
    dna = ('A', 'T', 'C', 'G')
    while count<len(seq):
        if seq[count] in dna:
            count += 1
        else:
            break
    if count != len(seq):
        print('This is not a DNA sequence')
        print('Enter a new one!')
        seq = validation()

    return seq


# Odd or Even lengths, in order to ensure that the target sequences keep their length
def o_e(s, x, y):
    if (y % 2) == 0:
        return s[x//2 - (y//2): x//2 + (y//2)]
    else:
        if (x % 2) != 0:
            return s[x//2 - (y//2): x//2 + (y//2) + 1]
        else:
            return s[x//2 - (y//2) - 1: x//2 + (y//2)]


# testing for match 2 nucleotides
def match (a, b):
    res = False
    if a == b:
        res = True
    return res


# It converts the indexes of matches from based to target sequences to based to the segment
# that the match is found. In the recursion function, the final converting to based on the initial sequences takes place
def fix_coors(x, seq, tseq, length):
    if len(seq) >= length:
        if length % 2 == 0:
            return x + len(seq) // 2 - (length // 2)
        else:
            if len(seq) % 2 == 0:
                return x + len(seq) // 2 - (length // 2) - 1
            else:
                return x + len(seq) // 2 - (length // 2)
    elif seq == tseq:
        return x
    else:
        return x + len(seq)


# Locates the parent match ,from which the segments that have been tested for the present much came from.
def previous_depth(lst, count):
    current = lst[count - 1]
    i = count - 2
    flag = False
    while i >= 0 and flag is False:
        z = lst[i]
        if current[0] - z[0] == 1:
            flag = True
        i -= 1
    return i+1


# This function calculates the length of the parts of sequences that the matches will be detected. It is settled
# as 5% of the initial length of the sequences and as 3 if this calculation returns a number lower than 3
def target_length(seq1, seq2):
    length = min(len(seq1), len(seq2))
    target = round(length * 5 / 100)
    if target < 3:
        target = 3
    return target
