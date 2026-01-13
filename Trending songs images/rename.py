import os
import re

folder_path = r"E:\Code\Javascript\Lecture 84 Project 2 Spotify Clone Website\Waqas's practice\Trending songs images"

image_pattern = re.compile(r".*\.jpg")
list_of_files = os.listdir(folder_path)

count = 1
for filename in list_of_files:
    old_path = os.path.join(folder_path, filename)
    if image_pattern.match(filename):
        new_filename = f"{count}.jpg"
        new_path = os.path.join(folder_path,  new_filename)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")
        count += 1