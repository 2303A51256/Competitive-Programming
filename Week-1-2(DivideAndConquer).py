def maxCrossingSum(arr, low, mid, high):
    summ = 0
    leftSum = -10**18
    
    for i in range(mid, low - 1, -1):
        summ += arr[i]
        if summ > leftSum:
            leftSum = summ
            
    summ = 0
    rightSum = -10**18
    
    for i in range(mid + 1, high + 1):
        summ += arr[i]
        if summ > rightSum:
            rightSum = summ
            
    return leftSum + rightSum

def maxProfitStreak(arr, low, high):
    if low == high:
        return arr[low]
        
    mid = (low + high) // 2
    
    return max(maxProfitStreak(arr, low, mid),
               maxProfitStreak(arr, mid + 1, high),
               maxCrossingSum(arr, low, mid, high))

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(maxProfitStreak(arr, 0, n - 1))