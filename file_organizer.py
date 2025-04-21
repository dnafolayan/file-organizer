import json
import sys
import time
from pathlib import Path


def load_file_mapping():
    try:
        with open("./file_map.json", "r") as file_mapping:
            global file_map

            file_map = json.load(file_mapping)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format: {e}")
        sys.exit(1)


folder_path = input("Please enter the full path to the folder to organize: ").strip()
working_dir = Path(folder_path)

if not working_dir.exists() or not working_dir.is_dir():
    print(f"Error: {working_dir} is not valid")
    sys.exit(1)


def create_folder(folder):
    folder_path = working_dir / folder

    if not folder_path.exists():
        try:
            folder_path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"Error creating folder '{folder_path}': {e}")
            sys.exit(1)


load_file_mapping()


def move_files():
    t1 = time.time()

    files = [item.name for item in working_dir.iterdir() if item.is_file()]

    for file in files:
        file_path = working_dir / file
        extension = file_path.suffix

        folder = file_map.get(extension, file_map["_"])

        create_folder(folder)

        destination_dir = working_dir / file_map.get(extension, file_map["_"])
        destination = destination_dir / file_path.name

        try:
            if destination.exists():
                print(f"Excluded {file}. Already exists in {destination_dir}")
                continue
            file_path.rename(destination)
            print(f"{file} moved to {destination_dir}/")

        except FileNotFoundError as e:
            print(f"{file_path} was not found. Error: {e}")
            sys.exit(1)

        except PermissionError as e:
            print(f"Permission denied for {file_path}. Error: {e}")
            sys.exit(1)

        except OSError as e:
            print(f"Failed to move {file_path}: {e}")
            sys.exit(1)

    t2 = time.time()
    print(f"Finished in {t2 - t1:.2f} seconds")


move_files()
