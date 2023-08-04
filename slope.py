def is_point_validation(point):
    valid = True
    error_message = ''
    if len(point) != 2:
        valid = False
        error_message = "invalid input please enter the point in x,y format"
        return (valid,error_message)
    elif len(point) >2:
        valid = False
        error_message = "invalid input please enter only x and y in x,y format "
        return (valid,error_message)
    return valid,''



first_point = input("enter the first point in x,y format")

first_point = first_point.split(',')

valid,error_messaage = is_point_validation(first_point)


if valid:
    
    print(error_messaage)

second_point = input("enter the first point in x,y format")

second_point = second_point.split(',')


valid,error_messaage = is_point_validation(second_point)

if valid:
    slope = second_point[2] - first_point[2]/ second_point[1] - first_point[1]
else:
    print(error_messaage)

print(slope)


