import shutil
import os

files_clean = {
   os.path.join(os.environ["USERPROFILE"], "OneDrive", "Desktop"),
   os.path.join(os.environ["USERPROFILE"], "Downloads"),
}

file_extentions = {
    "Images": [ ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg" ],
    "Videos": [ ".mp4", ".avi", ".mov", ".wmv", ".flv" ],
    "Documents": [ ".pdf", ".docx", ".txt", ".ppsx", ".xlsx", ".csv" ],
    "Audio": [ ".mp3", ".wav", ".flac" ],
    "Archives": [ ".zip", ".rar", ".tar", ".gz" ],
    "EXE": [".exe"]
}

def file_organizer(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if os.path.isdir(file_path):
            print(f"Skipping file: {filename}")
            continue

        file_extention_name = os.path.splitext(filename)[1].lower()
        moved = False

        for catogery, extention in file_extentions.items():
            if file_extention_name in extention:
                destination = os.path.join(folder, catogery)

                if not os.path.exists(destination):        
                    os.makedirs(destination)

                shutil.move(file_path, os.path.join(destination, filename))
                print(f"Moved {filename} to {destination}")
                moved = True
                break
        
        if not moved:
            print(f"No extention found for {filename}")
        
for n in files_clean:
    file_organizer(n)
    
print("File Organization was successfully completed!")
