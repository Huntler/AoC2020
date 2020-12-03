def parse_input(f, d="\n"):
    with open(f) as o:
        _ = o.read().split(d)
        _ = [z.split(" ") for z in _]
        x = []
        for r in _:
            d = {}
            d["letter"] = r[1][:-1]
            d["passwd"] = r[2]
            a = r[0].split("-")
            d["min"] = int(a[0])
            d["max"] = int(a[1])
            x.append((d))
        return x


def policy_counter(x):
    c = 0
    for _ in x:
        if _["min"] <= _["passwd"].count(_["letter"]) <= _["max"]:
            c += 1

    return c

def second_policy_counter(x):
    c = 0
    for _ in x:
        if _["passwd"][_["min"]-1] == _["letter"] and _["passwd"][_["max"]-1] != _["letter"]:
            c += 1

        elif _["passwd"][_["min"]-1] != _["letter"] and _["passwd"][_["max"]-1] == _["letter"]:
            c += 1

    return c

if __name__ == "__main__":
    x = parse_input("input.txt")
    print(policy_counter(x))
    print(second_policy_counter(x))