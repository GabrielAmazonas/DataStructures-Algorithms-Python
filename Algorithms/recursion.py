def get_fibonacci(position):
    if position == 0 or position == 1:
        return position
    else:
        return get_fibonacci(position - 1) + get_fibonacci(position - 2)


print(get_fibonacci(9))
print(get_fibonacci(11))
print(get_fibonacci(0))
