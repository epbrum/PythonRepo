script,filename=argv
#script=("main.py")
#filename=("file.txt")

txt=open(filename)
print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again=input("> ")

txt_again=open(file_again)

print(txt_again.read())