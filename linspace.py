
def linspace(start, end=0, step=1):
    if start > end:
        start, end = end, start
    while start < end:
        yield start
        start += step

if __name__ == '__main__':
    print("original python range generator")
    print("it can't generate float range")
    for i in range(1, 10):
        print(i, end=" ")
    print()
    print("linspace example 1~10")
    for i in linspace(1, 10):
        print(i, end=" ")
    print()
    print("linspace example 10~1")
    for i in linspace(10, 1):
        print(i, end=" ")
    print()
    print("linspace example 1~10 step 2")
    for i in linspace(1, 10, 2):
        print(i, end=" ")
    print()
    print("linspace example 1~2 step 0.1")
    for i in linspace(1, 2, 0.1):
        print(f"{i:.2f}", end=" ")
    print()
    print("linspace example -1~1 step 0.1")
    for i in linspace(-1, 1, 0.1):
        print(f"{i:.2f}", end=" ")
    print()