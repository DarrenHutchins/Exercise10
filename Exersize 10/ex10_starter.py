import glob
import os
import sys

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern

print("Construct a portable wild card pattern")
pattern = os.path.join(hdir,'*.*')
print(pattern)


# TODO: Use the glob.glob() function to obtain the list of filenames

print(glob.glob(pattern))

# TODO: use os.path.getsize to find each file's size
for f in glob.glob(pattern):
    print(f, os.path.getsize(f))

# TODO: Add a test to only display files that are not zero length
for f in glob.glob(pattern):
    if os.path.getsize(f) < 0:
        print(f, os.path.getsize(f))

# TODO: Remove the leading directory name(s) from each filename before you print it using os.path.basename()
for f in os.path.basename(f):
    filename = os.path.basename(f)
    print(filename)

# using os.path.basename()


