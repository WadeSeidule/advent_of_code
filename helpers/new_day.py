import shutil
import sys
import pathlib
import datetime
import os

def main() -> None:
    curr_dir = pathlib.Path(__file__).parent.resolve()
    year = datetime.datetime.now().year
    day = sys.argv[1]

    # create dir
    folder = f"{curr_dir}/../{year}/{day}"
    if not os.path.exists(folder):
        os.makedirs(folder)

    # create files
    files_to_create = (f'{folder}/input.txt', f'{folder}/answer.txt')
    for file in files_to_create:
         if not os.path.exists(file):
            open(file, 'w').close()

    shutil.copyfile(f'{curr_dir}/template.py', f'{folder}/{day}.py')

    print(f"created: {year}/{day}")


if __name__ == "__main__":
    main()