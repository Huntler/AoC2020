def parse_input(f, d="\n"):
    with open(f) as o:
        _ = o.read().split(d)
        return _

def policy(l, p):
    def run(x_step, y_step):
        x_pos = 0
        tree = 0
        for i in range(y_step, len(l), y_step):
            x_pos += x_step
            if l[i][x_pos % len(l[i])] == '#':
                tree += 1

        return tree

    trees = 1
    for _ in p:
        t = run(_[0], _[1])
        print(f"Policy: {_} has found {t} trees.")
        trees *= t

    return trees

if __name__ == "__main__":
    x = parse_input("input.txt")
    print(x)

    t = policy(x, [(3, 1)])
    print(f"Result puzzle 1 {t}")

    t = policy(x, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])
    print(f"Result puzzle 2 {t}")