import re


def parse_game(st: str) -> int:
    tries = [i.strip() for i in st.split(";")]
    list_games = [
        {i.split()[1]: int(i.split()[0]) for i in tri.split(", ")} for tri in tries
    ]
    power = 1
    for color in ("red", "blue", "green"):
        power *= max([game.get(color, 0) for game in list_games])
    return power


cumsum = 0
with open("2/input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        # print(line)
        game_id = re.search(r"Game (\d+):", line).group(1)
        games = re.search(r"Game \d+: (.*)", line).group(1)
        cumsum += parse_game(games)
print(cumsum)
