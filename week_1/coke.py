due = 50

while True:

    print ("Amount due:" , due)
    money = int(input("Insert coin: "))
    if money not in [25,10,5]:
        print ("Amount due:" , due)
    else:
        due = due - money

    if due <= 0:
        print("change owed:", abs(due))
        break
    else:
        continue
  

    
        
    