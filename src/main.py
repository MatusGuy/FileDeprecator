# 11/09/2022
# @gigtih

deprecated_symbols = [
    "game:GetService",
    "task.wait",
    ":FindFirstChild",
    ":Destroy"
    # "game"
]

DEPRECATOR_VERSION = "0.3"

selected = input("Welcome to the file deprecator. Please select a option: [D] to deprecate (must be a luau file), [V] for the version\n")
lowerinput = selected.lower().strip()

def deprecate_file(pathToFile: str):
    if not(".lua" in pathToFile):
        raise("File does not contain .lua")

    with open(pathToFile, "r") as file:
        deprecated_file_path = input("Please insert the path & name of the deprecated file: ")
        file_content = file.readlines()
        print("\nDEPRECATING...")
        with open(deprecated_file_path + ".lua", 'w') as deprecatedFile:
            deprecatedFile.write("--[[ File deprecated with file deprecator by gigtih, https://github.com/gigtih/FileDeprecator Version: {0} ]]\n\n".format(str(DEPRECATOR_VERSION)))

            for lineContent in file_content:
                for func in deprecated_symbols:
                    if func in lineContent:
                        deprecatedFile.write(lineContent.replace("game:GetService", "Game:service"))
                        continue
                    else:
                        deprecatedFile.write(lineContent)

            deprecatedFile.close()

        file.close()
        print("\n{0} was successfully deprecated, deprecated file can be found at: {1}".format(file.name, deprecatedFile.name))

    return

if lowerinput == 'd':
    file_path = input("Great! Now please insert a path to a file: ")
    deprecate_file(file_path.strip())
elif lowerinput == 'v':
    print("The current deprecator version is: " + DEPRECATOR_VERSION)