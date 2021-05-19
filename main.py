# Batch rename - initial release - 19.05.2021
# Rename files of given extension in given dir, disregard folders.

import os

# what we want to replace
search = "Name"
replace = "Shit"
extension = '.txt'

# get files from given directory
os.chdir('./files')
print(f'Current working directory: {os.getcwd()}')
dir_content = os.listdir('.')   # '.' - current dir
docs = [doc for doc in dir_content if os.path.isfile(doc)]
renamed = 0

print(f"{len(docs)} of {len(dir_content)} elements are files.")

# Iterate through all files and check if their name contains 'search':
for doc in docs:
    # check if extension is right:
    # doc_name, filetype = os.path.splitext(doc)
    # if filetype != extension:
    #     continue
    # Another way to check extension:
    if not doc.endswith('.txt'):
        continue

    # neat way to check if name contains 'search' string:
    if search in doc:
        new_name = doc.replace(search, replace)
        os.rename(doc, new_name)
        renamed += 1

        print(f"Renamed file '{doc}' to '{new_name}'.")

print(f"Renamed {renamed} files out of {len(docs)} files.")
