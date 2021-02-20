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

def mana_cal(ini,max):
        mana = max-ini
        t_time = mana*120
        return t_time

def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds) 

def souls(level):
        souls= level*3
        seal = math.ceil(souls/5)
        price = (souls*27500)+(seal*60000)
        return [souls,seal,price]
               
