def my_func(string):
    if len(string) < 6:
        return "Недостатньо символів"
    else:
        return string[:3] + string[-3:]
print(my_func("helloworldbeatifulworld"))
print(my_func("sdf"))