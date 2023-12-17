import re

load = {"red": 12, "green": 13, "blue": 14}


def parse_game(st: str) -> bool:
    tries = [i.strip() for i in st.split(";")]
    for tri in tries:
        pdict = {i.split()[1]: int(i.split()[0]) for i in tri.split(", ")}
        for key in pdict:
            if key not in load:
                return False
            if pdict[key] > load[key]:
                return False
    return True


cumsum = 0
with open("2/input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        # print(line)
        game_id = re.search(r"Game (\d+):", line).group(1)
        games = re.search(r"Game \d+: (.*)", line).group(1)
        if parse_game(games):
            cumsum += int(game_id)
print(cumsum)
