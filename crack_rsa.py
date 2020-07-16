import argparse
from math import sqrt
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e",type=int)
    parser.add_argument("-n",type=int)
    parser.add_argument("-c",type=int)
    return
if __name__ == '__main__':
    main()
def factorize(n):
    for x in range(2,int(sqrt(n))+1):
        if n%x == 0:
            return x, n//x
def modinverse(e, Q):
    g, a, b = egcd(e, Q)
    if g == 1:
        return int(a % Q)
def egcd(x, y):
    if x == 0:
        return y, 0, 1
    else:
        g, a, b = egcd(y % x, x)
        return g, b - (y//x)*a, a

def decrypt(d,n,c):
    m=c**d % n
    return m

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", type=int)
    parser.add_argument("-n", type=int)
    parser.add_argument("-c", type=int)
    args = parser.parse_args()
    p,q = factorize(args.n)
    Q = (p-1)*(q-1)
    d = modinverse(args.e, Q)
    m=decrypt(d,args.n,args.c)
    print(m)
    return
if __name__ == '__main__':
    main()