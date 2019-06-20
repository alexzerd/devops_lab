print("Input list of numbers")

keys = list(map(int, input().split()))

values = list(map(int, input().split()))

keys_length = len(keys)

values_length = len(values)

dictionary = {}

for i in range(keys_length):

    if i < values_length:

        dictionary[keys[i]] = values[i]

    else:

        dictionary[keys[i]] = "None"


print(dictionary)
