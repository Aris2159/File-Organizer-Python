#import the libraries thats are needed

import os
import shutil

folders_to_clean = [
    os.path.expanduser("~/Downloads"),
    os.path.expanduser("~/Desktop"),
]

file_extension = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx',  ],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.alac', '.ogg'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv']
}

def organize_folder(folder):
    for n in os.listdir(folder):
        ittem_path = os.path.join(folder, n)

        # Check if the item is a file or a folder
        if os.path.isdir(ittem_path):
            # If it's a folder, skip it
            print(f"Skipping folder: {n}")
        else:
            # If its a file then we check the extention if it matches
            # One of the extention in the file_extension dict and move 
            # it to the folder where we want that file to move to
            file_extension_name = os.path.splitext(n)[1].lower()
            for folderName, extention in file_extension.items():
                if file_extension_name in extention:
                    destination = os.path.join(folder, folderName)
                    break
            else:
                destination = os.path.join(folder, "Other")
                    
            if not os.path.exists(destination):
                os.makedirs(destination)
                shutil.move(ittem_path, destination)
                print(f"moved {n} to {destination}")
# Loop through the folders we want to clean and organize them
for folder in folders_to_clean:
    organize_folder(folder)    
print("Organizing completed!")