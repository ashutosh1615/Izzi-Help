import math
def add(operator,x,y):
        return x+y
def subtract(operator,x,y):
        return x-y
def divide(operator,x,y):
        return x/y
def multiply(operator,x,y):
        return x*y
def power(operator,x,y):
        return x**y
def card(start,end):
    exp=0
    for i in range(start,end):
        exp = exp+math.floor(10*(i**1.5))
    silver = math.ceil(exp/200)
    gold= math.ceil(exp/250)
    platinum = math.ceil(exp/300)
    return (exp,silver,gold,platinum)        

               
