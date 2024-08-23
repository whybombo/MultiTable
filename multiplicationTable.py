number = int(input("Enter the number: "))
#
#range(a,b) a is inclusive, b is not
# 
for mul in range(1,13) :
    print("{0} * {1} = {2}".format(number,mul, (number * mul)))