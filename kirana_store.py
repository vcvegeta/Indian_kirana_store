sum=0
while True:
    item_price=input("Enter item price or press 'q' to quit:\n")
    if item_price=='q':
        print(f"Your total bill is: {sum} , Thanks for shopping with us!")
        break
    else:
        sum=sum+int(item_price)
        print(f"Your sum as of now is: {sum}")


