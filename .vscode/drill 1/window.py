def window_max(num, k):
    sum = 0
    ans = []
    for i in range(len(num)):
        sum += num[i]
        if i >= k - 1:
            if i > k - 1:
                sum -= num[i-k]
            ans.append(sum)
    return ans
print(window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))