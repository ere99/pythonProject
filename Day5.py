
def my_discount():
    price = float(input("What is the price?; "))
    discount = float(input("What percentage is your discount?: "))
    aft_dsc = price - (price * discount/100)
    return 'Price after discount is ', aft_dsc


print(my_discount())
