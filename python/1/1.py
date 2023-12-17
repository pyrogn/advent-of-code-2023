def parse_line(line: str) -> int:
    line = line.strip()
    digits = [int(sym) for sym in line if sym.isdigit()]
    return digits[0] * 10 + digits[-1]


cumsum = 0
with open("1/input1.txt") as f:
    for line in f.readlines():
        cumsum += parse_line(line)
print(cumsum)
