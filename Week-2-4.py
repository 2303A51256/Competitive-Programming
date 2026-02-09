def subset_sum(arr, target, index=0, current_sum=0):
    if current_sum == target:
        return True
    if current_sum > target or index == len(arr):
        return False
    if subset_sum(arr, target, index + 1, current_sum + arr[index]):
        return True
    if subset_sum(arr, target, index + 1, current_sum):
        return True
    return False
n = int(input())
arr = list(map(int, input().split()))
target = int(input())
print(subset_sum(arr, target))