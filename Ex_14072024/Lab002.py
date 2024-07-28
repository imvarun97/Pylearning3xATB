import os

# get workdir, changedir, fileexist, filename, sizefile


print(os.name)
# nt- Window

print(os.getcwd())
# M:\3xATB\Pylearning3xATB\Ex_14072024

size = os.path.getsize('testdata.txt')

if size != 0:
    print("File exists")
else:
    print('No file')

# directory = os.getcwd()
# print(directory)
# if directory:
#     os.mkdir(r'M:\test')

for root, dir,files in os.walk(r"M:\3xATB\Pylearning3xATB\Ex_14072024"):
    print(f"Root directory: {root}")
    print(f"current directory: {dir}")
    print(f"files in the  directory: {files}")

