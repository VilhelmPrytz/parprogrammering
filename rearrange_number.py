def rearranged_difference(num):
    num_list = [d for d in str(num)]
    highest = sorted(num_list, reverse=True)
    lowest = sorted(num_list)

    return int("".join(highest)) - int("".join(lowest))

print(rearranged_difference(972882))
print(rearranged_difference(3320707))
print(rearranged_difference(90010))
