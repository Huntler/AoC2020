def parse_input(f, d="\n"):
    with open(f) as o:
        _ = o.read().split(d)
        return [int(z) for z in _]

def get_pair(l, s=2020):
    for i, n in enumerate(l):
        for j, m in enumerate(l):
            if i != j and n+m == s:
                return n, m, n*m

if __name__ == "__main__":
    x = parse_input("input_1.txt")
    y = get_pair(x)
    print(f"value pair: {y[0:2]} resulted in: {y[-1]}")