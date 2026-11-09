def longest_common(nums1, nums2):
    x = len(nums1)
    y = len(nums2)
    dp = [[0 for _ in range(x + 1)] for _ in range (y + 1)]
    for i in range(y):
        for j in range(x):
            if nums2[i] == nums1[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[y][x]

print(longest_common([101, 102, 99, 103, 104], [102, 99, 100, 104]) )