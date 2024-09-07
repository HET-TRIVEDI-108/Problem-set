# #PROtip=None 0 INDOOR VOICE
msg = str(input("enter the message :"))

msg: str = msg.lower()

print(f"{msg}")

#PROBLEM SET O PLAYBACK SPEED
messge  = str(input ())

messge: str = messge.replace(" ", "...")

print (messge)
from pickletools import long1


#PROBLEM SET MAKING FACES
def main():
    msg = input()

    result = convert (msg)

    print (result)

def convert(msg):

        msg = msg.replace(":)","🙂")

        msg = msg.replace(":(", "🙁")

        return  msg

main()

# PROBLEM SET 0 EINSTEIN
m = int(input("enter the value of mass i.e. m"))
c: int = 3 * pow(10, 8)

e: int = (m) * (pow(c, 2))

print(f"{e}")

#PROBLEM SET 0 TIP A MEAL
# def main():
#     dollars = dollars_to_float(input("how much was your meal : "))
#     percent = percent_to_float(input("how much percent of meal you want to tip : "))
#     tip = dollars * percent
#     print(f"leave ${tip:.3f}")
#
#     def dollars_to_float(dollars):
#         dollar_to_float = dollars.replace("$", "")
#         return float(dollar_to_float)
#
#     def percent_to_float(percent):
#         percent_to_float = percent.replace("%", "")
#         converted: float = float(percent_to_float) / 100
#         return converted
#
#     main()
