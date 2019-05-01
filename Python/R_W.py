from sys import argv
script, filename = argv

print(f"We are going to erase file {filename}")
print("If you don't want to erase, hit crtl+C (^C).")
print("If you do want to erase, hit RETURN.")

input("?")

print("Opening the file..")
target = open(filename,'w')

print("Truncating the file. Goodbye!.")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print("We are closing file now.")
target.close()


file_name = input(">") 
updated_target = open(file_name)
print(updated_target.read())