'''
Project Euler Problem #18

By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

Find the maximum total from top to bottom of the triangle in p18.txt
'''
RED = '\x1b[91m'
GREEN = '\x1b[92m'
RESET = '\x1b[0m'

def do_triangle(triangle):
    ''' Find the maximum total '''
    last_row = triangle[-1]
    new_row = []

    for row in triangle[-2::-1]:
        for i, v in enumerate(row):
            new_row.append(max(v+last_row[i], v+last_row[i+1]))
        last_row = new_row
        new_row = []
    return last_row[0]

def do_triangle_and_path(triangle):
    ''' Find the maximum total and the path taken to reach that total '''
    last_row = [(v,(i,)) for i,v in enumerate(triangle[-1])]
    new_row = []

    for row in triangle[-2::-1]:
        for i, v in enumerate(row):
            new_row.append((max(v+last_row[i][0], v+last_row[i+1][0]),
                            [last_row[i][1] + (i,), last_row[i+1][1] + (i,)][last_row[i] < last_row[i+1]])
            )
        last_row = new_row
        new_row = []
    return last_row[0]
    
def read_triangle(fname):
    triangle = []
    with open(fname, 'r') as f:
        for line in f.readlines():
            line = line.rstrip().split()
            triangle.append(list(map(int, line)))
    return triangle

def print_triangle(triangle, path):
    path = path[::-1]
    for tri_idx, row in enumerate(triangle):
        print(' ' * (((len(triangle[-1]) - len(row)) * 4) // 2), end='')
        for row_idx, v in enumerate(row):
            print('  {}{:02}{}'.format(RED, v, RESET) if row_idx == path[tri_idx] else '  {:02}'.format(v), end='')
        print()
    
if __name__ == '__main__':
    triangle = read_triangle('p18.txt')
    # print('{}Sum:{} {}'.format(GREEN, RESET, do_triangle(triangle)))
    result, path = do_triangle_and_path(triangle)
    print_triangle(triangle, path)
    print('{}Sum:{} {}'.format(GREEN, RESET, result))
