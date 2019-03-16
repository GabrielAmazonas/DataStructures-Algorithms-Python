def get_fibonacci(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    else:
        return get_fibonacci(position - 1) + get_fibonacci(position - 2)


print(get_fibonacci(9))
print(get_fibonacci(11))
print(get_fibonacci(0))
