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

    import re

    byr = re.compile("[0-9]{4}")
    if byr.match(p["byr"]) and not (1920 <= int(p["byr"]) <= 2002):
        return False

    iyr = re.compile("[0-9]{4}")
    if iyr.match(p["iyr"]) and not (2010 <= int(p["iyr"]) <= 2020):
        return False

    eyr = re.compile("[0-9]{4}")
    if eyr.match(p["eyr"]) and not (2020 <= int(p["eyr"]) <= 2030):
        return False

    hgt = re.compile("[0-9]*(cm|in)")
    if hgt.match(p["hgt"]):
        h = int(p["hgt"][:-2])
        if p["hgt"].endswith("cm") and not (150 <= h <= 193):
            return False
        elif p["hgt"].endswith("in") and not(59 <= h <= 76):
            return False

    hcl = re.compile("#([0-9a-f]){6}")
    if not hcl.match(p["hcl"]) or len(p["hcl"]) != 7:
        return False

    #ecl = re.compile("(amb|blu|brn|gry|grn|hzl|oth)")
    if p["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    pid = re.compile("[0-9]{9}")
    if not pid.match(p["pid"]) or len(p["pid"]) != 9:
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
