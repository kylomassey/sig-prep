import bisect
def running_median(nums):
    med = []
    arr = []
    n = len(nums)
    for i in range(n):
        if not arr:
            arr.append(nums[i])
        else:
            bisect.insort(arr,nums[i])
        cnt = i + 1
        if cnt % 2 == 1:
            med.append(arr[cnt // 2])
        else:
            print(cnt)
            sum = arr[cnt // 2] + arr[(cnt // 2) - 1]
            med.append(sum / 2)
    return med
print(running_median([5, 15, 1, 3]))