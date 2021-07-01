
# function to convert centimeters to inches
def convert_inches():
    centimeter = float(input("Enter the height in Centimeters: "))
    inches=0.394 * centimeter
    print("The height in inches", round(inches, 2))

# function to convert inches to centimeters
def convert_centimeters():
    inch = float((input("Enter the height in Inches: ")))
    centimeters = inch/0.394
    print("The height in Centimeters", round(centimeters, 2))

# user options
print("1: Centimeters to Inches")
print("2: Inches to Centimeters")

option = int(input("Enter Your Option: "))

# condition to run the option
if option == 1:
    convert_inches()
elif option == 2:
    convert_centimeters()
else:
    print("Invalid Option")



