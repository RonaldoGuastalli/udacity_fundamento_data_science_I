'''
Quiz: Implementando my_enumerate
Escreva sua própria função de gerador que funciona como a função interna enumerate.
'''

lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    """Implement your generator function here"""
    count = start
    for element in iterable:
        yield count, element
        count += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))


