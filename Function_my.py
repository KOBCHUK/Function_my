#Напишіть функцію, яка приймає рядок
# та повертає рядок з першою літерою кожного слова,
#написаним великими літерами
def my_func(string):
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)
my_func("hello world")
