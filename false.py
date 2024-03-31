if set():
    print("This won't be printed.")

if dict():
    print("This won't be printed.")

if []:
    print("This won't be printed.")

if "":
    print("This won't be printed.")

if 0:
    print("This won't be printed.")

if tuple():
    print("This won't be printed.")

if None:
    print("This won't be printed.")

if False:
    print("This won't be printed.")


list = [1, 2, 3, 4]

while list:
    print(list.pop())
    

