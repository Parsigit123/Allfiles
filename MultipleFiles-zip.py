contents = ["This is the text for file 1",
            "This is the text for file 2",
            "This is the text for file 3"]

filenames = ["file01.txt", "file02.txt", "file03.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)
    print(filename, " " , content, " which Has ", len(content), "Character")
    file.close()

