
seq = input("Enter Sequence Number: ")
num1 = input("Enter First Number: ")
num2 = input("Enter Second Number: ")

total_sum = 0

for index in range(int(seq)):
    if total_sum == 0:
        total_sum = int(num1) + int(num2)
        print(total_sum)

    else:

        total_sum = int(total_sum) + int(num2)
        num2 = int(total_sum) - int(num2)
        print(total_sum)

