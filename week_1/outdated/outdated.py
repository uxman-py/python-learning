months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    while True:
        user_input = input("Date: ")
        if "/" in user_input:
            try:
                parts = user_input.split("/")
                month = int(parts[0])
                day = int(parts[1])
                year = int(parts[2])

                if month>12 or month<1:
                    raise ValueError
                elif day < 1 or day > 31:
                    raise ValueError
                
                print (f"DATE: {year:04}-{month:02}-{day:02}")
                break
        
            except (ValueError):
                print("Enter a correct date.")
                continue
        else:
            try:
                parts = user_input.split()
                month = parts[0]
                if not parts[1].endswith(","):
                    raise ValueError

                day = int(parts[1].strip(","))
                year = int(parts[2])

                if month not in months:
                    raise ValueError
                elif day < 1 or day > 31:
                    raise ValueError
                
                month_number = months.index(month)+1

                print (f"DATE: {year:04}-{month_number:02}-{day:02}")
                break
            
            except (ValueError, IndexError):
                print("Enter a correct date.")
                continue

main()
            


            


        


    

          