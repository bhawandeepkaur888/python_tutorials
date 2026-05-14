# file handling in python
# python can read, write, and manipulate files
# always use 'with' statement (context manager) for safe file handling

import os
import pathlib

# file open modes:
# "r"  - read (default), raises error if file doesn't exist
# "w"  - write, creates file or overwrites existing
# "a"  - append, adds to end of file
# "x"  - exclusive create, raises error if file exists
# "r+" - read and write
# "b"  - binary mode (e.g., "rb", "wb")

# ---- WRITING TO A FILE ----
print("writing to file :")

with open("demo.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is file handling.\n")
    file.write("Line three.\n")

print("demo.txt created and written")


# writing multiple lines at once
lines = ["Line one\n", "Line two\n", "Line three\n"]
with open("demo_lines.txt", "w") as file:
    file.writelines(lines)

print("demo_lines.txt written with writelines()")


# ---- READING FROM A FILE ----
print("\nreading from file :")

# read entire file as string
with open("demo.txt", "r") as file:
    content = file.read()
    print("read() output :\n", content)


# read line by line
with open("demo.txt", "r") as file:
    print("readline() outputs :")
    line = file.readline()
    while line:
        print(f"  {repr(line)}")
        line = file.readline()


# read all lines into a list
with open("demo.txt", "r") as file:
    all_lines = file.readlines()
    print("\nreadlines() :", all_lines)


# iterate line by line (memory efficient)
with open("demo.txt", "r") as file:
    print("\niterating over file :")
    for line in file:
        print(f"  {line.strip()}")


# ---- APPENDING TO A FILE ----
print("\nappending to file :")

with open("demo.txt", "a") as file:
    file.write("Appended line.\n")

with open("demo.txt", "r") as file:
    print("file after append :\n", file.read())


# ---- FILE POSITION (seek and tell) ----
print("\nfile position :")
with open("demo.txt", "r") as file:
    print("initial position :", file.tell())
    content = file.read(5)
    print("read 5 chars :", repr(content))
    print("position after read :", file.tell())
    file.seek(0)                     # go back to start
    print("position after seek(0) :", file.tell())
    first_line = file.readline()
    print("first line :", first_line.strip())


# ---- os.path - FILE UTILITIES ----
print("\nos.path file utilities :")
print("file exists :", os.path.exists("demo.txt"))
print("is file :", os.path.isfile("demo.txt"))
print("is directory :", os.path.isdir("demo.txt"))
print("file size :", os.path.getsize("demo.txt"), "bytes")
print("absolute path :", os.path.abspath("demo.txt"))


# ---- pathlib - modern path handling ----
print("\npathlib :")
from pathlib import Path

p = Path("demo.txt")
print("Path object :", p)
print("name :", p.name)
print("stem :", p.stem)
print("suffix :", p.suffix)
print("parent :", p.parent)
print("exists :", p.exists())
print("is_file :", p.is_file())

# read and write with pathlib
p.write_text("Written by pathlib!\n")
content = p.read_text()
print("pathlib read_text :", content.strip())


# ---- WORKING WITH DIRECTORIES ----
print("\nworking with directories :")

# create directory
os.makedirs("demo_folder/subfolder", exist_ok=True)
print("created demo_folder/subfolder")

# list directory contents
print("demo_folder contents :", os.listdir("demo_folder"))

# rename file
if not os.path.exists("demo_renamed.txt"):
    os.rename("demo_lines.txt", "demo_renamed.txt")
    print("renamed demo_lines.txt to demo_renamed.txt")


# ---- BINARY FILE HANDLING ----
print("\nbinary file handling :")

# write binary data
with open("demo.bin", "wb") as f:
    f.write(bytes([72, 101, 108, 108, 111]))   # bytes for "Hello"

# read binary data
with open("demo.bin", "rb") as f:
    binary_data = f.read()
    print("binary data :", binary_data)
    print("decoded :", binary_data.decode("utf-8"))


# ---- CLEANUP: remove demo files ----
for fname in ["demo.txt", "demo_renamed.txt", "demo.bin"]:
    if os.path.exists(fname):
        os.remove(fname)

import shutil
if os.path.exists("demo_folder"):
    shutil.rmtree("demo_folder")

print("\ndemo files cleaned up")
print("\nall file handling concepts demonstrated successfully")
