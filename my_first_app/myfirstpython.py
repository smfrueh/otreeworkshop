price = 100
garden_price = 1000

def house_price(length, width):
    space = length * width
    return space * price

def elite_house_price(length, width):
    return  house_price(length, width) + garden_price

my_house_price = elite_house_price (10,20)
print (my_house_price)
a = house_price(10,10)
print (a)

a = [(10,20),(20,30), (30, 40)]
b = [house_price (i[0],i[1]) for i in a]
print (b)