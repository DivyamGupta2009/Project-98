def swapFileData():
    firstFile = input("Enter the name of the first file: ")
    with open(firstFile, 'r') as a:
        data_a = a.read()
    secondFile = input("Enter the name of the second file: ")
    with open(secondFile, 'r') as b:
        data_b = b.read()
    with open(firstFile, 'w') as a:
        a.write(data_b)
    with open(secondFile, 'w') as b:
        b.write(data_a)
    print("Data is switched.")

swapFileData()





