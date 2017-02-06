records = {
    'foo': None,
    'bar': None,
    'baz': 1
}

for _ in range(100):
    records['baz'] += 1

for k in records.items():
    print(str(k))
