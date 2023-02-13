"""Dict"""

dct1 = {}
dct2 = dict()

print(type(dct1), type(dct2))

dct1["key1"] = "Value1"

print(dct1)

dct1["key1"] = "Value2"

print(dct1)

dct3 = {(1, 2):"List1"}

print(dct3)

dct4 = {str(i):i for i in range(10)}

print(dct4)