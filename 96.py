from copy import deepcopy
f = open('sudoku.txt', 'r')
filelines = f.read().split('\n')
N = 50
string_to_list = lambda s: [c for c in s]
filelines = [string_to_list(l) for l in filelines]
sudokus = [filelines[i*10:(i+1)*10][1:] for i in range(N)]

f.close()

def square(sudoku, i, j):
    start_line, start_col = (i/3)*3, (j/3)*3
    return (sudoku[start_line][start_col:start_col+3] + 
            sudoku[start_line+1][start_col:start_col+3] +
            sudoku[start_line+2][start_col:start_col+3])

def candidates(sudoku, i, j):
    if sudoku[i][j] != '0': return None
    return [n for n in '123456789'
              if not n in sudoku[i]
              if not n in [line[j] for line in sudoku]
              if not n in square(sudoku, i, j)]

def print_sudoku(sudoku):
    print '#'*31
    for i in range(9):
        if not i%3: print '-'*31
        line = ''
        for j in range(9):
            if not j%3: line += '|'
            line += ' %s ' % sudoku[i][j]
        print line + '|'
    print '#'*31
    print ''

def new_guess(sudoku, i, j, value):
    new  = deepcopy(sudoku)
    new[i][j] = value
    return new

def solve(sudoku):
    while True:
        zeros_left = False
        current_min, next = 9, None
        some_change = False
        for i in range(9):
            for j in range(9):
                c = candidates(sudoku, i, j)
                if not c is None:
                    zeros_left = True
                    if len(c) == 1:
                        sudoku[i][j] = c[0]
                        #print_sudoku(sudoku)
                        some_change = True
                    elif len(c) == 0:
                        print 'bug somewhere'
                        return None
                    elif len(c) < current_min:
                        current_min, next = len(c), (i,j)
        if not zeros_left: break
        if not some_change:
            line, col = next
            cand = candidates(sudoku, line, col)
            print 'Splitting guesses %s-%s: %s' % (line, col, ' '.join(cand))
            print_sudoku(sudoku)
            try:
                return filter(lambda x: not x is None,
                          [solve(new_guess(sudoku, line, col, c)) for c in cand])[0]
            except Exception:
                return None
    return sudoku

sudoku = solve(sudokus[0])
print 'Result:'
print_sudoku(sudoku)

def problem_96():
    result = 0
    for n, sudoku in enumerate(sudokus):
        print 'Solving %s ...' % n
        result += sum([10**(2-i)*int(c) for i, c in enumerate(solve(sudoku)[0][:3])])
    return result

print problem_96()

