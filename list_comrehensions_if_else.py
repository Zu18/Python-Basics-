# Given a list of filenames, rename all the files with extension hpp to the extension h.
# Generate a new list called newfilenames, consisting of the new filenames.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames,
# cut the last two characters off if a string ends with "hpp"
newfilenames = [file[0:-2] if file.endswith("hpp") else file for file in filenames]
print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
