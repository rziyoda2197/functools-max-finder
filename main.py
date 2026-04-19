from functools import partial

def max_finder(talabalar, key):
    return max(talabalar, key=key)

talabalar = [
    {"ism": "Ali", "ball": 90},
    {"ism": "Vali", "ball": 80},
    {"ism": "Hasan", "ball": 95},
    {"ism": "Husan", "ball": 85}
]

max_finder = partial(max_finder, key=lambda x: x["ball"])

print(max_finder(talabalar))
