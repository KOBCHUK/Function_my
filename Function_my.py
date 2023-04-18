def string():
    list = [1,2,3,4,5,6,7,8,9,10]
    print(list)
    print(sum(list)/len(list))
string()

def average(list):
    return sum(list)/len(list)
print(average([1,2,3,4,5,6,7,8,9,10]))

def arithmetic_mean(numbers):
  
    if not numbers:
        return 0
    else:
        return sum(numbers) / len(numbers)

print(arithmetic_mean([1,2,3,4,5,6,7,8,9,10]))
