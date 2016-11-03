#4
#aba
#baba
#aba
#xzxb
#3
#aba
#xzxb
#ab


def string_occured(strings, queries):

    # Store count
    count = 0
    i = 0

    # Loop over all the queries and print their individual count at the end
    while i < len(queries):

        for j in strings:
            if j in queries[i]:
                count += 1

        print count
        count = 0
        i += 1

# Store data from input
n = int(raw_input())
strings = []
queries = []

for i in xrange(n):
    # Loop over n strings from input
    strings.append(str(raw_input()))

q = int(raw_input())

for i in xrange(q):
    # Loop over q strings from input
    queries.append(str(raw_input()))

#strings = ['aba', 'baba', 'aba', 'xzxb']
#queries = ['aba', 'xzxb', 'ab']
print string_occured(strings, queries)
