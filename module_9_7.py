# Декораторы
def is_prime(func):
    def wrapper(*args):
        result_func = func(*args)
        print('Простое' if all([result_func % i for i in range(2, result_func // 2 + 1)]) else 'Составное')
        return result_func
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)