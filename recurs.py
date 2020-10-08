import os


def fib(n):
    fib_prev = 0
    fib_cur = 1
    i = 0
    while i < n-1:
        fib_sum = fib_prev + fib_cur
        fib_prev = fib_cur
        fib_cur = fib_sum
        i += 1
    return fib_cur


print(fib(12))


def fib_rec(n):
    if n in (1, 2):
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


print(fib_rec(12))


def walk(path):

    dirs_list = os.walk(path)
    for root, dirs, files in dirs_list:
        for folder in dirs:
            print(os.path.join(root, folder))
        for file in files:
            print(os.path.join(root, file))


walk("f1")
