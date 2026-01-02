
# x = int(input("Enter number of rows: "))
# y  = int(input("Enter number of rows: "))
# a = int(input("Enter spaces:"))

# sum = 0
# for i in range(x):
#     i += 1
#     sum += i
#     for j in range(a - i):
#         print(" ", end="")
#     for k in range(i):
#         print("* ", end="")
#     print()


# sum = 0
# for y in range(y,0 ,-1):
#     y -= 1
#     sum += y
#     for j in range(a - y):
#         print(" ", end="")
#     for k in range(y):
#         print("* ", end="")
#     print()

x = int(input("Enter number of rows: "))
a = int(input("Enter spaces:"))
sum = 0
for i in range(x):
    i += 1
    sum += i
    for j in range(a - i):
        print(" ", end="")
    for k in range(i):
        print("* ",)
    print()