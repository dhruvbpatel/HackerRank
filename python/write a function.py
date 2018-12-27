# write a function that checks whether the year is leap or not
def is_leap(year):
    leap = False
    
    #  logic
    if(year%4==0):
        if(year%100==0):
            leap=False
            if(year%400==0):
                leap=True
        else:
            leap=True
    else:
        leap=False                

    return leap

year = int(input())
print(is_leap(year))
