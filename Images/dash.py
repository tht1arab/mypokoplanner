import os

ROOT_FOLDER = r"C:\Users\layal\OneDrive\Desktop\poke planner\mypokoplanner\Images"

renamed = 0

for root, dirs, files in os.walk(ROOT_FOLDER):

    for filename in files:

        if "-" not in filename:
            continue

        old_path = os.path.join(root, filename)
        new_name = filename.replace("-", "")
        new_path = os.path.join(root, new_name)

        # avoid overwriting if file already exists
        if not os.path.exists(new_path):

            os.rename(old_path, new_path)
            print("RENAMED:", filename, "→", new_name)
            renamed += 1

print(f"\nDone. Renamed {renamed} files.")