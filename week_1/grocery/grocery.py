list = {}

while True:
    try:
        
        user = input("Item: ").strip().upper()
        if not user:
            print("Enter items.")
            continue
        if user in list:
            list[user] += 1
        else:
            list[user] = 1
        continue
    
    except EOFError:
        print()

        sorted_list = dict(sorted(list.items()))

        for item , quantity in sorted_list.items():
            print(f"{quantity} {item}")

        break




    