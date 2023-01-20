
Freezing_point = 0
Boiling_point = 100

def state(temp):
    if temp <= Freezing_point:
        return "Ice"
    elif Freezing_point < temp < Boiling_point:
        return "Liquid"
    else:
        return "Gas"

#print(state(10))
