import math

def number_of_days(orders, size):
    days = 0
    total = 0
    for o in orders:
        if total + o > size:
            total  = 0
            days += 1
        total += o
    return days + 1 if total > 0 else days

def min_capacity(orders, k):
    if not orders:
        return 0
    l = max(orders)
    r = sum(orders)

    while l <= r:
        mid = math.ceil((l+r) / 2)
        if number_of_days(orders, mid) > k:
            l = mid + 1
        elif number_of_days(orders, mid) <= k:
            r = mid - 1
    return mid

print(min_capacity([3, 2, 2, 4, 1, 4], 3))
