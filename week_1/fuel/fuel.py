def main():
    while True:
        user = input("Fraction: ")
        try:
            prev = user.split("/")
            x = int(prev[0])
            y = int(prev[1])
            if x > y and y>0:
                print("do not enter an improper fraction.")
                continue
            elif x < 0:
                print("enter a positive fraction.")
                continue 
            percentage = round((x/y) * 100)
            break
    
        except (ZeroDivisionError, ValueError):
            print ("Do not divide by 0 and only enter integers.")
            continue

    if percentage <= 1 and percentage >=0:
        print("E")
    elif percentage >= 99:
        print ("F")
    else:
        print (f"{percentage}%")


main()