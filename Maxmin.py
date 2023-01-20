# def get_maxmin():
#     grades = [9.6, 9.2, 9.7]
#     max_local = max(grades)
#     min_local = min(grades)
#     maxmin = [max_local, min_local]
#     return maxmin
#
# print("The maximum is: ", get_maxmin()[0], '\n', "and the minimum is: ", get_maxmin()[1])


def get_maxmin():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    message = f"Max: {maximum}, Min: {minimum}"
    return message


print(get_maxmin())
