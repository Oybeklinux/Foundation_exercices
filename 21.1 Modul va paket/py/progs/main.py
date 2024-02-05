import sys
sys.path.append("..\\mods")
sys.path.append("..\\modules")


import mat

mat.sin()
for path in sys.path:
    print(path)