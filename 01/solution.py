def parse_input(f, d="\n"):
    with open(f) as o:
        _ = o.read().split(d)
        return [int(z) for z in _]

def get_pair_1(l, s=2020):
    for i, n in enumerate(l):
        for j, m in enumerate(l):
            if i != j and n+m == s:
                return n, m, n*m

def get_pair_2(l, s=2020):
    for i, b in enumerate(l):
        for j, n in enumerate(l):
            for k, m in enumerate(l):
                if i != j and j != k and n+m+b == s:
                    return b, n, m, b*n*m

if __name__ == "__main__":
    x = parse_input("input.txt")
    y = get_pair_1(x)
    print(f"value pair: {y[0:2]} resulted in: {y[-1]}")

    y = get_pair_2(x)
    print(f"value triplet: {y[0:3]} resulted in: {y[-1]}")