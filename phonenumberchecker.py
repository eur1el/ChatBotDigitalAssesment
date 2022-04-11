def check_phone(question, ph_low, ph_high):
    while True:
        try:
            num = int(input(question))
            test_num = num
            count = 0
            while test_num > 0:
                test_num = test_num//10
                count = count + 1
            if count >= ph_low and count <= ph_high:
                return str(num)
            else:
                print("NewZealand mobile numbers contain 7 to 10 digits")
        except ValueError:
            print("Please enter a number ")