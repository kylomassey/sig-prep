def longest_balanced(line):
    n = len(line)
    cumsum = [0] * (n + 1)
    idx = {}
    total = 0
    for i in range(n):
        if line[i].upper() == 'B':
            cumsum[i+1] = cumsum[i] + 1
        elif line[i].upper() == 'S':
                    cumsum[i+1] = cumsum[i] - 1
    for n in range(len(cumsum)):
        if cumsum[n] not in idx:
            idx[cumsum[n]] = n
        else:
            total = max(total, n - idx[cumsum[n]])
    return total
            
print(longest_balanced("SBBBSBBS"))