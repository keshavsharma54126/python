with open("example.txt", "r") as file:
    content = file.read()
    print(content)

with open("example.txt", "w") as file:
    file.write("This is a line.\n")
    file.write("This is another line.\n")
