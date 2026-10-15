file = open("example.txt", "w")
file.write("Hello, World!")
file.close()

file = open("example.txt", "r")
content = file.read()
print(content)

file.close()

file = open("example.txt", "a")
file.write("\nThis is an appended line.")
file.close()

file = open("example.txt", "r")
content = file.read()   
print(content)
file.close()