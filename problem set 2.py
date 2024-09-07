# def main():
#     print_square(3)
#
# def print_square(size):
#
#         for i in range(size):
#             for j in range(size):
#                 print("#", end = "")
#             print()
#
#
# if __name__ == '__main__':
#     main()
from pickle import FLOAT

# PROBLEM SET 2 CAMEL CASE
# camelcase = input("CamelCase : ")
# print("snakeCase : ", end="")
# for _ in camelcase:
#
#     if _.isupper():
#         print("_" + _.lower(), end="")
#
#     else :
#         print(_ , end="")
#
#
# print()

def sum_of_digits(number):

    # Convert the number to a string to iterate over each digit
    str_number = str(number)

    # Calculate the sum of digits
    total = sum(int(digit) for digit in str_number)
    return total

number = int(input("Enter a positive integer: "))
result = sum_of_digits(number)
print(f"The sum of the digits is: {result}")