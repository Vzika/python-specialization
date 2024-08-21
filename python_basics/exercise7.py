#WAP to attend to peoples order of pizza
#TAKE INPUT FROM USER asking the size of piza they want
#small pizza 100
#meduim pizza 200
#large piza 300
#pepperoni for small piza 30
#pepperoni for big pizza and meduim pizza 50
# extra cheese for any of the pizza 20
# output thier totall bill based on thier order

def pizza_order():
    order = input("Do you want to buy pizza? Enter YES or NO: ").strip().lower()
    
    # Prices
    small_pizza_price = 100
    medium_pizza_price = 200
    large_pizza_price = 300
    pepperoni_small_price = 30
    pepperoni_medium_large_price = 50
    extra_cheese_price = 20

    if order == "yes":
        size_of_pizza = input("What size of pizza do you want? Small is 100, Medium is 200, & Large is 300: ").strip().lower()
        total_amount = 0

        if size_of_pizza == "small":
            total_amount += small_pizza_price
            pepperoni = input("Do you want pepperoni 30? Answer YES or NO: ").strip().lower()
            if pepperoni == "yes":
                total_amount += pepperoni_small_price
            else:
                print("Try using pepperoni next time, it's nice.")
                
        elif size_of_pizza == "medium":
            total_amount += medium_pizza_price
            pepperoni = input("Do you want pepperoni 50? Answer YES or NO: ").strip().lower()
            if pepperoni == "yes":
                total_amount += pepperoni_medium_large_price

        elif size_of_pizza == "large":
            total_amount += large_pizza_price
            pepperoni = input("Do you want pepperoni 50? Answer YES or NO: ").strip().lower()
            if pepperoni == "yes":
                total_amount += pepperoni_medium_large_price

        else:
            print("Invalid pizza size. Please choose Small, Medium, or Large.")
            return

        extra_cheese = input("Do you want extra cheese @ 20? Answer YES or NO: ").strip().lower()
        if extra_cheese == "yes":
            total_amount += extra_cheese_price
        else:
            print("Extra cheese is nice, try it next time.")

        print(f"Your total amount is {total_amount}")
    else:
        print("Order from us next time! Goodbye!")

# Call the function to execute the code
pizza_order()

