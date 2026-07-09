def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    seen_a_letter = False
    prev_char = ""

    if not s[0:2].isalpha():
        return False
    elif len(s) > 6 or len(s)< 2:
        return False
    for i in s:
        if not i.isalnum():
            return False
    for i in reversed(s):
        if seen_a_letter and i.isdigit():
            return False
        elif i.isalpha():
            if prev_char == "0":
                return False
            seen_a_letter = True
        prev_char = i
   
    return True

main()