# Дано натуральное число N. Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.

number = int(input("Введите любое число: "))
primes = []


while number > 1:
    for j in range(2, int(number) + 1):
        if number % j == 0:
            number /= j
            primes.append(j)
            break

print(f"{primes} Количество чисел: {len(primes)}")