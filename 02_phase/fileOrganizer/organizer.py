import os 
import shutil
folder ="02_phase/fileOrganizer/testfolder"
files = os.listdir(folder)

folders = {
    ".jpg": "Images",
    ".png": "Images",
    ".jpeg": "Images",

    ".pdf": "PDFs",

    ".txt": "Text",

    ".mp4": "Videos",

    ".mp3": "Audio",

    ".py": "Python"
}


for file in files:
    path = os.path.join(folder , file)

    if not os.path.isfile(path):
        # print(file)
        continue
    name , ext = os.path.splitext(file)
    # print(name)
    folder_name = folders.get(ext, "Others")
    destination = os.path.join(folder , folder_name)








if not os.path.exists(destination):
    os.mkdir(destination)


# print(name)
# print(extension)



extension = ".pdf"
# print(folders[extension])


# lets create a folder
