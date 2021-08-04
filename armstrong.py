num = int(input("no"))
sum = 0
temp = num
while temp > 0:
    no = temp % 10
    sum += no ** 3
    temp //= 10

if num == sum:
    print(num, "arn")
else:
    print(num, "not")
