import Sort


# This function counts gaps, matches and mismatches are present in an alignment
def counts(s1, s2):
    gaps, m, mm = 0, 0, 0
    for i in range(len(s1)):
        if s1[i] == '-' or s2[i] == '-':
            gaps += 1
        elif s1[i] == s2[i]:
            m += 1
        else:
            mm += 1
    return gaps, m, mm


# This Function calculates the score of an alignment
def score(s1, s2):
    d = -2
    match = 1
    missmatch = -1
    gaps, m, mm = counts(s1, s2)
    return gaps * d + match * m + missmatch * mm


# This function recursively deletes one by one the matches that have been found and tests if a better score is
# calculated. Every time that the score is increased the current match is permanently deleted, otherwise it is added
# back. This recursion consumes the most of the time of the whole process
def improved_score(seq1, seq2, s1, s2, coors):
    max_score = score(s1, s2)
    max_s1, max_s2 = s1, s2
    max_coors = coors[:]
    for i in range(len(coors)):
        a = coors[i]
        del coors[i]
        new_s1, new_s2 = Sort.total_alignment(coors, seq1, seq2)
        new_score = score(new_s1, new_s2)
        if new_score > max_score:
            max_s1 = new_s1
            max_s2 = new_s2
            max_coors = coors[:]
            max_score, max_s1, max_s2, max_coors = improved_score(seq1, seq2, max_s1, max_s2, max_coors)
        coors.insert(i, a)
    return max_score, max_s1, max_s2, max_coors


# This function calculated the percentages of matches, mismatches and gaps in the final alignment
def percentage(s1, s2):
    g, m, mm = counts(s1, s2)
    matches = round(m / len(s1) * 100, 2)
    mismatches = round(mm / len(s1) * 100, 2)
    gaps = round(g / len(s1) * 100, 2)
    print('Alignment status')
    print('Matches: ', matches, '%')
    print('Mismatches: ', mismatches, '%')
    print('Gaps: ', gaps, '%')
    return matches, mismatches, gaps
