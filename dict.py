# my_d = {
#   "name": "Joe",
#   "foo": 343,
#   "my_items": [1, 2, 4324, "fewfw"],
#   (1,2): "some string"
# }

# # print(my_d[(1,2)])

# my_d["name"] = [23, 123]

# # del my_d["name"]

# for key, value in my_d.items():
#   print(f"my_d has key {key} and its value is {value}")

# --------------------------------
# ----- Dictionary Challenge ----- 
# --------------------------------

our_dictionary = {
    "name": "Joe",
    "age": 25,
    "value": "This is some text",
    "foo": "bar",
    3: "test",
    (1, 2): "test2",
    "items": ["test", 1, 2, 6, "one"],
    "another_random_value": False,
    "set_1": {0, 1, 2, 4, 4},
    "odd_thing": {"length": 34, "area": 600},
    "nothing": None,
}

t = ("name", "foo", "nothing", "odd_thing", "set_1")

# We're not getting the "Nothing"!
# for item in t:
#   if our_dictionary.get(item):
#     print("------------------------")
#     print(f"our_dictionary has the key {item}")
#     print(f"The value of the key is {our_dictionary[item]}")
#     print("------------------------")

for item in t:
  if item in our_dictionary.keys():
    print("------------------------")
    print(f"our_dictionary has the key {item}")
    print(f"The value of the key is {our_dictionary[item]}")
    print("------------------------")