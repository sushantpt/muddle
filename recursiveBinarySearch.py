# binary search (recursive implementation)
from random import randint
l = [randint(1,50) for i in range(20)]
ll = sorted(l)
print(ll)
def binary_implementation(dataset, to_find, low, high):
    if low <= high:
        mid = (low + high) // 2
        if to_find == dataset[mid]:
            return True
        elif to_find < dataset[mid]:
            return binary_implementation(dataset, to_find, low, mid - 1)
        elif to_find > dataset[mid]:
            return binary_implementation(dataset, to_find, mid + 1, high)
    else:
        return False
result1 = binary_implementation(ll, 23, 0, len(ll)-1)
print(result1)
