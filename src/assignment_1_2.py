def divide(dividend, divider, operation=""):
    if operation == "modulus":
        return dividend % divider
    elif operation == "floor_division":
        return dividend // divider
    else:
        return dividend / divider

def main():
    print("11 / 4 = ", divide(11, 4))
    print("11 // 4 = ", divide(11, 4, "floor_division"))
    print("11 % 4 = ", divide(11, 4, "modulus"))

main()