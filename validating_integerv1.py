def ordertype():
    while True:
        try:
            num = int(input())
            if num >= 1 and num <= 2:
                return num
            else:
                print ("The numerical value must be 1 or 2")
        except ValueError:
            print ("That is not a valid value")
            print ("Please enter 1 or 2")

print("Please enter a numerical value between 1 and 2")

answer = ordertype()

print(answer)