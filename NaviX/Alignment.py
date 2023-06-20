import MainRecursion
import Sort
import Score
import Time_Memory
import time
import Files
import Basics

coors = []


def align(seq1, seq2):
    TARGET_L = Basics.target_length(seq1, seq2)
    print('The length of the target segments', TARGET_L)
    global coors
    time_start = time.perf_counter()
    coors = MainRecursion.div_and_conq(seq1, seq2, coors, TARGET_L, depth=0)
    matches = len(coors)
    print('Matches detected in the first phase: ', matches)
    if len(coors) >= 1:
        coors = Sort.sort(coors)
        s1, s2 = Sort.total_alignment(coors, seq1, seq2)
        score, s1, s2, coors = Score.improved_score(seq1, seq2, s1, s2, coors)
        print('The score of the alignment is :', score)
        time_elapsed = Time_Memory.time_calc(time_start)
        memory = Time_Memory.mem_calc()
        m_perc, mm_perc, gaps_perc = Score.percentage(s1, s2)
        f = open("Results.txt", "a")
        Files.file_handling(f, time_elapsed, memory, score, m_perc, mm_perc, gaps_perc)
        f.close()
    else:
        print('No matches found!!!')
