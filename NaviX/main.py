import Basics
import Alignment

print('Enter 1 for entering the sequences in terminal or 2 for uploading from different files')
selection = input()
if selection == '1':
    seq1 = Basics.validation()
    seq2 = Basics.validation()
else:
    seq1 = open("seq1.txt", "r").read()
    seq2 = open("seq2.txt", "r").read()
Alignment.align(seq1, seq2)
