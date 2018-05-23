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

a = {'name':'seraina', 'middle name': 'madlaina' ,'surname':'frueh'}
print(a['middle name'])
numbers = [(3,3),(4,4),(5,5), (6,6),(7,7)]
def adding_numbers(n1, n2):
    addition = n1 + n2
    return (addition)
b = [adding_numbers (i[0],i[1]) for i in numbers]   # => [6, 7]
print(b)
