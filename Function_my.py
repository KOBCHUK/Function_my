def my_func(string):
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)
print(my_func("hello world beatiful world"))
