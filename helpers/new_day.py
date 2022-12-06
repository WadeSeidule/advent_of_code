import shutil
import pathlib
import datetime
import os
import requests
import argparse

CURR_DIR = pathlib.Path(__file__).parent.resolve()
AOC_URL = "https://adventofcode.com"
INPUT_TEMPLATE = "{url}/{year}/day/{day}/input"

LANGUAGES = {
    "python": f'{CURR_DIR}/templates/template.py',
    "go": f'{CURR_DIR}/templates/template.go'
}

def get_input(year: str, day: int) -> str:
    input_url = INPUT_TEMPLATE.format(url=AOC_URL, year=year, day=day)
    with open(f'{CURR_DIR}/cookie.txt') as f:
        cookie = f.read().strip()
    res = requests.get(input_url, cookies={"session": cookie})
    return res.text.strip()


def main() -> None:

    parser = argparse.ArgumentParser()
    parser.add_argument('--day', type=int, required=True)
    parser.add_argument('--language', default='python', choices=list(LANGUAGES.keys()))
    parser.add_argument('--year', default=datetime.datetime.now().year)
    args = parser.parse_args()

    year, day = args.year, args.day

    # create dir
    folder = f"{CURR_DIR}/../{year}/day{day}"
    if not os.path.exists(folder):
        os.makedirs(folder)

    # get input and create input file
    puzzle_input = get_input(year, day)
    with open(f'{folder}/input.txt', 'w') as f:
        f.write(puzzle_input)

    # create empty answer file for storage
    open(f'{folder}/answer.txt', 'w').close()

    # copy template python script to created folder
    shutil.copyfile(LANGUAGES[args.language], f'{folder}/day{day}.py')

    print(f"created: {year}/{day}")


if __name__ == "__main__":
    main()