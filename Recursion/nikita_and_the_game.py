def findMaxMoves(ele, sum):
    '''
    1. Calculate the sum first time and divide by 2
    2. Start from first index and keep adding elements till you get (sum/2),thats your partition,
    3. Now send both partitions in same function and find maximum between two.
    * Special case when string is all '0's in that case its just len(elementlist)-1.
    * I am sending sum as parameter to avoid further sum calculations from list
    '''
    sum = sum / 2
    if sum == 0:
        if ele<> [0 for x in xrange(0,len(ele))]:
            return 0
        else:
            return len(ele)-1
    s = 0
    i = 0
    n = len(ele)
    if len(ele) == 1 or len(ele) == 0:
        return 0
    while s <> sum and i < n:
        s += ele[i]
        i += 1
    if i >= n:
        return 0
    return 1 + max(findMaxMoves(ele[0:i], sum), findMaxMoves(ele[i:n], sum))


def main():
    T = int(raw_input())
    for i in xrange(0, T):
        global dict
        N = raw_input()
        ele = [int(x) for x in raw_input().split()]
        print findMaxMoves(ele, sum(ele))
main()
