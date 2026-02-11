import os
import shutil


def move_file(command: str) -> int:

    args = command.split(" ")

    if len(args) != 3:
        return 1

    if args[0] != "mv":
        return 1

    source_path = os.path.abspath(args[1])
    source_file = source_path.split("/")[-1]

    if args[2].endswith("/"):
        args[2] += source_file

    dest_path = os.path.abspath(args[2])

    try:
        os.makedirs(dest_path.rstrip(args[2]), exist_ok=True)
        shutil.move(source_path, dest_path)
    except OSError:
        return 1
    else:
        return 0
