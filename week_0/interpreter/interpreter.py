expression = input("Expression: ")

x = int(expression[0])
y = expression[2]
z = int(expression[4])

match y:
    case _ if y == "+":
        sum = x + z
        print(f"{sum:.1f}")
    case _ if y == "-":
        sum = x - z
        print(f"{sum:.1f}")
    case _ if y == "*":
        sum = x * z
        print(f"{sum:.1f}")
    case _ if y == "/":
        sum = x / z
        print(f"{sum:.1f}")
    case _:
        print("False Expression!")
        
    



