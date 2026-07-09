file = input("Enter the name of the file: ")
match file:
    case _ if file.endswith(".gif"):
        print("image/gif")
    case _ if file.endswith(".jpg"):
        print("image/jpg")
    case _ if file.endswith('.jpeg'):
        print("image/jpeg")
    case _ if file.endswith('.png'):
        print("image/png")
    case _ if file.endswith('.pdf'):
        print("image/pdf")
    case _ if file.endswith('.txt'):
        print("image/txt")
    case _ if file.endswith(".zip"):
        print("image/zip")
    case _:
        print("application/octet-stream")
