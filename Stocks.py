import math
# import round
# Program that calculates -3% of a number and +10% of a number
# example: number is 100 and answer is 97 and 110
# gain = float(0.1)
# loss = float(-0.03)

# buy = input('input buy order')

# tobuy = gain * buy
# toloss = loss * buy

# print(tobuy)

# print(toloss)

def Stocks():
    my_number = float(input("Enter your number "))
    my_gain = 10 / 100 * my_number
    my_loss = -3 / 100 * my_number

    number_gain = round(my_number + my_gain, 2)
    number_loss = round(my_number + my_loss, 2)
   

    # print(f'Your gain from the number {my_number} is  +{my_gain}, and your loss is -{my_loss}')
    print(f'you gained {number_gain} and you lost {number_loss}')

Stocks()