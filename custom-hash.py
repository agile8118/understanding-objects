def hash_str(string):
    final = 0
    for i in string:
        final += ord(i) * 438575382

    return final % 1000000000


def hash_int(integer):
    return (integer * 588375111) % 1000000000


def hash_tuple(t, final=0):
    if len(t) == 0:
        return 71538492
    for item in t:
        if isinstance(item, (str)):
            final += hash_str(item)

        if isinstance(item, (int)):
            final += hash_int(item)

        if isinstance(item, (tuple)):
            final += hash_tuple(item, final)

    return final % 1000000000


def custom_hash(value):
    if isinstance(value, (str)):
        return hash_str(value)

    if isinstance(value, (int)):
        return hash_int(value)

    if isinstance(value, (tuple)):
        return hash_tuple(value)


my_value = (2, 8, 1128973981272, ("fsdF", "more"), 121, 123213, 12312, "efwf")

print(custom_hash(my_value))
print(custom_hash(my_value))
print(custom_hash(my_value))
print(custom_hash(my_value))
print(custom_hash(my_value))
print(custom_hash(my_value))
print(custom_hash(my_value))
print(custom_hash(my_value))

# my_value[0] = 123
