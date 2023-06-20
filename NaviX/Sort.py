# Sorts the list with the paired-indexes of the matches.
def sort(l1):
    n = len(l1)
    for i in range(1, n):
        x1 = l1[i]
        value = l1[i][0]
        j = i
        for j in range(i, -1, -1):
            if l1[j - 1][0] > value:
                l1[j] = l1[j-1]
            else:
                break
        l1[j] = x1
    return l1


# Creates the final alignment by adding '-', where  gaps appear
def total_alignment(lst, seq1, seq2):
    start = lst[0]
    if start[0] == 0 and start[1] == 0:
        s1, s2 = seq1[0], seq2[0]
    elif start[0] > start[1]:
        s1, s2 = seq1[: start[0] + 1], (start[0] - start[1]) * '-' + seq2[: start[1] + 1]
    else:
        s2, s1 = seq2[: start[1] + 1], (start[1] - start[0]) * '-' + seq1[: start[0] + 1]
    lst.append([len(seq1), len(seq2)])
    for i in range(0, len(lst) - 1):
        begin, end = lst[i], lst[i + 1]
        d0, d1 = end[0] - begin[0], end[1] - begin[1]
        if d0 > d1:
            s1 += seq1[begin[0] + 1: end[0] + 1]
            s2 += (d0 - d1) * '-' + seq2[begin[1] + 1: end[1] + 1]
        else:
            s2 += seq2[begin[1] + 1: end[1] +1]
            s1 += (d1 - d0) * '-' + seq1[begin[0] +1: end[0] +1]
    return s1, s2
