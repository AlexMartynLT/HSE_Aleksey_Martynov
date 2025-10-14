def fib(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        a, b = b, a + b

# проверяем функцию
fib(10) 

def fib_generator(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

print('Проверяем генератор:')
for number in fib_generator(10):
    print(number)
