import numpy as np

def parse_input(f, d="\n"):
    with open(f) as o:
        _ = o.read().split(d)
        return [int(z) for z in _]

def get_pair(l, s=2020):
    for i, n in enumerate(l):
        for j, m in enumerate(l):
            if i != j and n+m == s:
                return i*j, n, m, n*m

def get_pair_optimized(l, s=2020):
    l = np.array(l)
    for i in range(len(l)):
        a = l + np.roll(l, i)
        if np.nonzero(a==s)[0].size != 0:
            j = np.nonzero(a==s)[0]
            return i, l[j][0], l[j-i][0], (l[j] * l[j-i])[0]

def get_triplet(l, s=2020):
    for i, b in enumerate(l):
        for j, n in enumerate(l):
            for k, m in enumerate(l):
                if i != j and j != k and n+m+b == s:
                    return i*j*k, n, m, b*n*m

def get_triplet_optimized(l, s=2020):
    l = np.array(l)
    for i in range(len(l)):
        for j in range(len(l)):
            a = l + np.roll(l, i) + np.roll(l, j)
            if np.nonzero(a==s)[0].size != 0:
                k = np.nonzero(a==s)[0]
                return i*j, l[k][0], l[k-i][0], l[k-j][0], (l[k] * l[k-i] * l[k-j])[0]

if __name__ == "__main__":
    x = parse_input("input.txt")
    y = get_pair(x)
    print(f"value pair: {y[1:3]} resulted in: {y[-1]} with {y[0]} iterations needed.")

    y = get_pair_optimized(x)
    print(f"value pair: {y[1:3]} resulted in: {y[-1]} with {y[0]} iterations needed. (optimized)")

    y = get_triplet(x)
    print(f"value triplet: {y[1:4]} resulted in: {y[-1]} with {y[0]} iterations needed.")

    y = get_triplet_optimized(x)
    print(f"value triplet: {y[1:4]} resulted in: {y[-1]} with {y[0]} iterations needed. (optimized)")