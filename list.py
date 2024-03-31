# ---------------------------
# ----- List Challenge  ----- 
# ---------------------------

our_list = [
    12,
    12,
    "Greg",
    "text",
    "more text",
    12,
    45,
    12,
    90,
    "Adam",
    43,
    12323,
    [12, 32, "this is another list"],
]

for index, item in enumerate(our_list):
  if item == "Adam":
    our_list[index] = item.upper()


print(our_list)