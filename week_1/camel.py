def main():
    camel = input("camel case: ")
    snake(camel)


def snake(phrase):
    for i in phrase:
        if i.isupper():
            phrase = phrase.replace(i , "_" + i.lower())
    print("snake case: ",phrase)


main()







