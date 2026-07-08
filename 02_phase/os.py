import os
# print(os.getcwd())  #get a current  working directory 
# print(os.listdir()) #list files
# print(os.listdir("/home/hassanraza/prototyping")) #list specifoc folder files

# os.mkdir("Python")  # creates a directory -folder
# os.makedirs("Projects/python")  # creates a directory with sub directory

# os.rmdir("Python")  # remove dir

# os.removedirs("projects/python/backend") # remove nested empty folders


#  rename of the file

# os.rename("old.txt", "new.txt")

# os.rename("Python", "pythonCourse")



# print(os.path.exists("main.py"))  # check if path exits

# print(os.path.isdir("images")) # check file  or directory
# print(os.path.isfile("main.py"))

# absolute path - gives full path 

# print(os.path.abspath("os.py"))

path = os.path.join("folder", "file.txt")

# print(path)



#  file name & extensions

path = "images/photo.png"

# print(os.path.basename(path)) # file name
# print(os.path.dirname(path)) # dir name

name ,ext = os.path.splitext(path)

# print(name)
# print(ext)


# environment variables

print(os.getenv("HOME"))







