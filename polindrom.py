
def polindrom():
    for n in range(10,1000000):
        if str(n)==str(n)[::-1] :
            print(n)


if __name__ == '__main__':
    polindrom()