# def get_farenheit():
#     celsius = [0, 10, 25, 30, 50, 70, 100]
#     list = []
#     for i in celsius:
#         list = list.append(i * 1.8 + 32)
#         print(list)
#     return (list)
#
# result = get_farenheit()
# print(result)
# print("Hi")

# def get_farenheit():
#     celsius = [0, 10, 25, 30, 50, 70, 100]
#     list2 = []
#     for i in celsius:
#         far = int(i * 1.8 + 32)
#         list2 = list2.append(far)
#     print(list2)
#     return list2
#
#
# result2 = get_farenheit()
# print(result2)

def get_farenheit():
    celsius = [0, 10, 25, 30, 50, 70, 100]
    for i in celsius:
        far = i * 1.8 + 32
        print(far)
    return far

list2 = []
result2 = get_farenheit()
list2 = list2.append(int(result2))
print(result2)
print(list2, " List")