#!/opt/homebrew/bin/python3
import os
import sys
import glob
import getpass
import hashlib

user = getpass.getuser()

sha256sum = "sha256sum"
keys=[]

def getSha(content):
    sha256 = hashlib.sha256()
    sha256.update(content)
    return sha256.hexdigest()
	# Defining main function
def scanDir(folder):
    files = []
    print(f"Scanning files in the directory: {folder}")
    for file in os.scandir(folder):
        if file.is_file():
            files.append( file.name )
    return files

def hashFiles(list, dir):
    for x in list:
        path = dir + x
        try:
            fileContent = open(path, 'r').read().encode('utf-8')
            print( f"{x:<60} : {getSha(fileContent):>10}" )
        except TypeError as e:
            print("String must be encoded before hashing. - ")
        except UnicodeDecodeError as e:
            print( f"{x:<60} : {'Could not create digest.':>10}" )

def main():
    scanFolder = ""
    defaultFolder = f"/Users/{user}/.ssh/"
    Direc = input(f"Enter the path of the folder: ({defaultFolder}")
    if Direc == "":
        scanFolder = defaultFolder
    else:
        scanFolder = Direc
    files = scanDir(scanFolder)
    hashFiles(files, scanFolder)

# Using the special variable
# __name__
if __name__=="__main__":
    main()



#returned_value = os.system('sha256sum ' + sys.argv[1])

#print('returned value:', returned_value)
