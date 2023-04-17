
#Створіть функцію, яка приймає
#ціле число та повертає список
#всіх дільників цього числа
def div_number(num):
    numbers = []
    for i in range(1, num + 1):
        if num % i == 0:
            numbers.append(i)
    return numbers
print(div_number(10))
print(div_number(234))
