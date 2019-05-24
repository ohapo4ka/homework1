def get_sum(num_one, num_two):
    try:
        return int(num_one) + int(num_two)
    except ValueError:
        return None

print(get_sum(2, 2))
print(get_sum(7, 'шиш'))