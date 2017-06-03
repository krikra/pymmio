import itertools

def _skipcomments(filename):
    f = open(filename, 'r')
    return(itertools.dropwhile(lambda x: x[0] == '%', f.readlines()))

def tocoo(filename):
    lines = _skipcomments(filename)
    M, N, nnz = map(int, next(lines).split(' '))
    col = []
    row = []
    val = []
    for l in lines:
        ll = l.split(' ')
        col.append(int(ll[0]) - 1)
        row.append(int(ll[1]) - 1)
        val.append(float(ll[2]))

    return(M, N, nnz, col, row, val)

def tocsr(filename, as_asymm=False):
    lines = _skipcomments(filename)
    M, N, nnz = map(int, next(lines).split(' '))
    ptr = [0]
    ind = []
    val = []
    row = 0
    for l in lines:
        ll = l.split(' ')
        ind.append(int(ll[0]) - 1)
        val.append(float(ll[2]))
        row_current = int(ll[1]) - 1
        if row + 1 == row_current:
            ptr.append(len(val) - 1)
            row = row_current

    ptr.append(nnz)

    return(M, N, nnz, ptr, ind, val)

def todense(filename, as_asymm=False):
    lines = _skipcomments(filename)
    M, N, nnz = map(int, next(lines).split(' '))
    A = [[0 for i in range(M)] for j in range(N)]
    for l in lines:
        ll = l.split(' ')
        col = int(ll[0]) - 1
        row = int(ll[1]) - 1
        val = float(ll[2])
        A[col][row] = val
        if as_asymm is True:
            A[row][col] = val

    return(M, N, nnz, A)
