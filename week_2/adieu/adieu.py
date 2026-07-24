import inflect
p = inflect.engine()
names = []

def main():
    while True:
        try:
           user = input("Name:")

           names.append(user)
           
        except EOFError:
            print()
            print(f"Adieu Adieu to {p.join(names)}")
            break
    

main()
        

