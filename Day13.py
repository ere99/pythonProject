def yur_vat():
    while True:
        try:
            price = int(input('What is the item price?: '))
            vat = int(input('What is the percentage vat?: '))
        except ValueError:
            print('Enter a valid number: ')
        else:
            total_price = price + (price * vat/100 + 1) - 1
            return 'The price Vat inclusive is', total_price


print(yur_vat())
