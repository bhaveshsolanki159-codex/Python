f = open("sample.txt", "r")
content = f.read()

# for counting characters
print(f"word : {len(content)}")

# for counting words
print(f"word : {len(content.split())}")

# for copying content of one file to another file
f = open("file.txt", "w")
f.write(content)

# for find and replace words
replaced = content.replace("is", "was")
print(replaced)



