menu ={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    sum = 0
    while True:
        try:
            user = str(input("Item: ").title())
            sum = sum + menu[user]
            print(f"Total: ${sum:.2f}")
            continue
       
        except ValueError:
            print("Enter names of items only: ")
            continue
        
        except EOFError:
            print("\nThank you for ordering :)")
            break
        
        except KeyError:
            print("\nEnter from menu only: ")
            continue
    
    
main()
    



            
