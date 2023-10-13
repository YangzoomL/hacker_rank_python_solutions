a =int(input("put in a x corodinate"))
b= int(input("put in another x corodinate"))
c= int(input("put in a y corodinate"))
d= int(input("put in another y corodinate"))

def calculate_slope(x1, y1, x2, y2):

    
    if x1 == x2:
        
        raise ValueError("The slope is undefined (vertical line).")
    else:
        slope = (y2 - y1) / (x2 - x1)
        return slope

calculate_slope(a, c, b , d)

try:
    slope = calculate_slope(a, c, b, d)
    print(f"The slope between ({a}, {c}) and ({b}, {d}) is: {slope}")
except ValueError as e:
    print(e)




