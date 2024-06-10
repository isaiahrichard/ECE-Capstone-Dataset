import os
import zipfile

# Absolute path to the root directory
root_dir = "E:\DMD\dmd"

# Walk through the directory structure
for group in os.listdir(root_dir):
    group_path = os.path.join(root_dir, group)
    if os.path.isdir(group_path):
        for number in os.listdir(group_path):
            number_path = os.path.join(group_path, number)
            if os.path.isdir(number_path):
                for sub in os.listdir(number_path):
                    sub_path = os.path.join(number_path, sub)
                    if os.path.isdir(sub_path):
                        # Find the zip file in the sub directory
                        for file in os.listdir(sub_path):
                            if file.endswith(".zip"):
                                zip_path = os.path.join(sub_path, file)
                                with zipfile.ZipFile(zip_path, "r") as zip_ref:
                                    zip_ref.extractall(sub_path)
                                print(f"Extracted {zip_path} into {sub_path}")
