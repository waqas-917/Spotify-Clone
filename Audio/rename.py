import os

folder_path = "E:\Code\Javascript\Lecture 84 Project 2 Spotify Clone Website\Waqas's practice\Audio"
text_to_remove = "(freetouse.com)"
list_of_files = os.listdir(folder_path)

for filename in list_of_files:
    old_path = os.path.join(folder_path, filename)
    if text_to_remove in filename:
        new_filename = filename.replace(text_to_remove, "").strip()
        new_path = os.path.join(folder_path,  new_filename)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")
    