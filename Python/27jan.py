# File Handling in Python
"""
syntax:
f = open("file path", "mode1mode2")
f.close()

Modes:
Mode 1:                             Mode 2: t: text mode, b: binary file
r   read                            t   text        Default
w   Write                           b   binary
a   append
x   exclusively create
r+  read plus
w+  write plus
a+  append plus
"""
# f = open("myfile1.txt")     # same as f = open("myfile.txt", "rt")
"""
m = f.read()
print(m)
print(f.tell())
f.seek(0)
print(f.tell())
"""
"""
a = f.readline()
print(a, type(a))
print(f.readline())
b = f.readlines()
print(type(b))
print(b)
print(f.readable())
print(f.writable())
f.close()
"""
"""
f = open("myfile.txt", "wt")        # same as f = open("myfile.txt", "w")
print(f.writable())
print("What do you want to write in file? Type here: (Press 'q' when you're done)")
myList = []
a = input()
while a != 'q':
    myList.append(a + "\n")
    a = input()

print(myList)
# f.write(a)
f.writelines(myList)
f.close()
"""
"""
f = open("myfile2.txt", "r")
f.close()
"""
"""
Mode 1:
r   Read Mode   Opens the file for reading only (Can't write).
                Raises FileNotFoundError if file does not exist.
                Places the cursor at the begining of the file.

w   Write Mode  Opens the file for writing only (Can't read).
                Creates the file if it does not exist.
                Places the cursor at the begining of the file.
                Clears the entire content of the file as soon as it opens the file.

a   append      Opens the file for writing only (Can't read).
                Creates the file if it does not exist.
                Places the cursor at the end of the file.
                Does not clear the content of the file.

x   Exclusive   Creates a new file and opens for writing only.   
    Create      Raises FileExistsError if the file already exists.
                Places the cursor at the begining of the file.

r+  read plus   Opens the file for reading and writing both.
                Raises FileNotFoundError if file does not exist.
                Places the cursor at the begining of the file.
                Does not clear the content of the file.

w+  write plus  Opens the file for writing and reading.
                Creates the file if it does not exist.
                Places the cursor at the begining of the file.
                Clears the entire content of the file as soon as it opens the file.

a+  append plus Opens the file for writing and reading.
                Creates the file if it does not exist.
                Places the cursor at the end of the file.
                Does not clear the content of the file.
"""
"""
f = open("myfile.txt", "a")        # same as f = open("myfile.txt", "w")
print(f.writable())
print(f.readable())
print("What do you want to write in file? Type here: (Press 'q' when you're done)")
myList = []
a = input()
while a != 'q':
    myList.append(a + "\n")
    a = input()

print(myList)
f.writelines(myList)
f.close()
"""
f = open("newfile.txt", "x")
print(f.writable())
print(f.readable())
f.close()