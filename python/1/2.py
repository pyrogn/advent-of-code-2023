s = "one, two, three, four, five, six, seven, eight, nine"
num_dict_o = {num_s: str(num_d) for num_d, num_s in enumerate(s.split(", "), 1)}
num_dict = {
    num_s: num_s + str(num_d) + num_s for num_d, num_s in enumerate(s.split(", "), 1)
}


def parse_line(line: str) -> int:
    line = line.strip()
    line_o = line
    line2 = line
    for num1, num2 in num_dict.items():
        line = line.replace(num1, num2)
    idx_num = {x: idx for x, y in num_dict_o.items() if (idx := line.find(x)) != -1}
    num_to_replace = {i: j for i, j in sorted(idx_num.items(), key=lambda x: -x[1])}
    if not num_to_replace:
        mm = range(10)
    else:
        mm = min(num_to_replace.values()), max(num_to_replace.values())
    for num_s, idx in num_to_replace.items():
        if idx in mm:
            line2 = line2[: idx - 1] + str(num_dict[num_s]) + line2[idx - 1 :]
    digits = [int(sym) for sym in line if sym.isdigit()]
    digits2 = [int(sym) for sym in line2 if sym.isdigit()]

    def asdf(x):
        return 10 * x[0] + x[-1]

    if asdf(digits) != asdf(digits2):
        print(line_o, digits, digits2, line2)
    return digits[0] * 10 + digits[-1]


cumsum = 0
# with open("1/test_input2.txt") as f:
with open("1/input1.txt") as f:
    for line in f.readlines():
        cumsum += parse_line(line)
print(cumsum)
