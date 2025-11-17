def sensor(people):
    count = 0
    result = ""
    for human in people:
        if human == "+":
            count +=1
        elif human == "-":
            count -=1
        
        if count >= 3:
            result = "True"
        else:
            result = "False"
    return result

data = input("Enter a data from the sensor: ")
print(sensor(data))