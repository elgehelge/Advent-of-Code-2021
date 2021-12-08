# Puzzle #1
input_ = open('08-1-input.txt').readlines()
digits = [d for line in input_ for d in line.split('|')[-1].split()]
print(len([d for d in digits if len(d) in [2, 4, 3, 7]]))
