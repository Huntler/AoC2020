def parse_input(f, d="\n"):
    with open(f) as o:
        _ = o.read().split(d)
        r = [[]]
        i = 0
        for v in _:
            if v == '':
                r.append([])
                i += 1
                continue

            r[i].append(v)
        r = [to_dict(i) for i in r]
        return r


def to_dict(a):
    f = sum([e.split(' ') for e in a], [])
    d = {}
    for e in f:
        p = e.split(":")
        d[p[0]] = p[1]

    return d


def is_valid(p):
    c = [x in p.keys() for x in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]]
    if False in c:
        return False

    try:
        if not (1920 <= int(p["byr"]) <= 2002):
            return False
    except:
        return False

    try:
        if not (2010 <= int(p["iyr"]) <= 2020):
            return False
    except:
        return False

    try:
        if not (2020 <= int(p["eyr"]) <= 2030):
            return False
    except:
        return False

    try:
        if p["hgt"].endswith("cm"):
            if not (150 <= int(p["hgt"][:-2]) <= 193):
                return False
        if p["hgt"].endswith("in"):
            if not (59 <= int(p["hgt"][:-2]) <= 76):
                return False
    except ValueError:
        return False

    try:
        if p["hcl"].startswith("#"):
            int(p["hcl"][1:], base=16)
            if len(p["hcl"]) != 7:
                return False
    except ValueError:
        return False

    if p["ecl"] not in ["amb", "blu", "brn", "gry", "hzl", "grn", "oth"]:
        return False

    try:
        int(p["pid"], base=10)
        if len(p["pid"]) != 9:
            return False
    except ValueError:
        return False

    return True


if __name__ == "__main__":
    x = parse_input("input.txt")
    print(f"Program detected {len(x)} passports.")
    c = 0
    for p in x:
        if is_valid(p):
            c += 1

    print(f"Found {c} valid passports.")
