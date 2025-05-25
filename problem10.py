def fibonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_series = [0, 1]
    count = 2

    while count < n:
        next_value = fib_series[-1] + fib_series[-2]
        fib_series += [next_value]
        count += 1

    return fib_series

# Test
print(fibonacci_series(7))  # Output: [0, 1, 1, 2, 3, 5, 8]
