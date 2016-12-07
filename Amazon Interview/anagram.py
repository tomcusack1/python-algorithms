from collections import Counter


def number_needed(a, b):
    counter_a = Counter(a)
    counter_b = Counter(b)
    counter_a.subtract(counter_b)
    return sum(abs(i) for i in counter_a.values())

string_one = str(raw_input())
string_two = str(raw_input())

print number_needed(string_one, string_two)
