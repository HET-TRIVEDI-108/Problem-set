
#PROBLEM SET 1 DEEP THINKING
# qolife = (input("What is answer to the Great Question of life,the Universe and Everything ? ")).strip().lower()
#
# if qolife == "42" or qolife == "forty-two" or qolife == "forty two" :
#     print("yes")
# else:
#     print("no")
from lib2to3.pytree import convert


#PROBLEM SET 0 HOME FEDERAL SAVINGS BANK
# def main():
#     greeting = input("enter your greetings : ").strip().lower()
#
#     if greeting.startswith("hello"):
#         print("$0")
#     elif greeting.startswith("h"):
#         print("$20")
#     else:
#         print("$100")
#
#
# if __name__ == "__main__":
#     main()

#PROBLEM SET 1 FILE EXTENSIONS
# def main():
#
#     filename1: str = input("enter the file name(along with the extension) : ").lower()
#
#     if filename1.endswith(".gif"):
#         print("Image/Gif")
#     elif filename1.endswith(("jpg","jpeg")):
#         print("Image/jpeg")
#     elif filename1.endswith(".png"):
#         print("Image/png")
#     elif filename1.endswith(".pdf"):
#         print("application/pdf")
#     elif filename1.endswith(".txt"):
#         print("text/plain")
#     elif filename1.endswith(".zip"):
#         print("application/x-7z-compressed")
#     else :
#         print("application/octet-stream")
#
# if __name__ == "__main__":
#     main()

# expression = input("enter the expression : ")
#
# x,y,z = expression.split("   ")
#
# new_x = float(x)
# new_z = float(z)
#
# if y == "+" :
#     result = new_x + new_z
# if y == "-" :
#     result = new_x - new_z
# if y == "/" :
#     result = new_x / new_z
# if y == "*" :
#     result = new_x * new_z
#
#     print(result)

#PROBLEM SET 1 MATH INTERPRETER
expression = input("enter the expression : ").strip()

x, y, z = expression.split(" ")

new_x = float(x)
new_z: float = float(z)

if y == "+" :
    result = new_x + new_z
if y == "-" :
    result = new_x - new_z
if y == "/" :
    result = new_x / new_z
if y == "*" :
    result = new_x * new_z

print(result)
