import os

# linux va windowsga mos
file = "../file"  # windows=c:/dir/file, linux = /dir/file
file_obj = open(file, mode ='br')
print(type(file_obj), type(file_obj).__bases__)
# Windows
file = "../file"
file_obj = open(file, mode ='tr')
print(type(file_obj), type(file_obj).__bases__)

print(os.path.exists(file))

# Windows
file = r"../file"
print(os.path.exists(file))
