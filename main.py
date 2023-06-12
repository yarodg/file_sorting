import os
import shutil
import glob


def main():
    patterns = ["txt", "csv", "md"]

    for pattern in patterns:
        files_list = glob.glob(f"*.{pattern}")
        print(files_list)

        for file in files_list:
            name, extension = file.split(".")
            create_folder(extension)
            shutil.move(file, extension)


def create_folder(extension):
    if not os.path.exists(extension):
        os.mkdir(extension)
        print(f"Created folder {extension}.")
    else:
        print(f"Folder {extension} exists.")


if __name__ == "__main__":
    main()
