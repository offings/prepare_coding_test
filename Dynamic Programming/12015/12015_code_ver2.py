n = int(input())
num_list = list(map(int, input().split()))
dp = [num_list[0]]

def binary_search(search):
    start = 0
    end = len(dp) - 1

    while start <= end:
        mid = (start + end) // 2
        if dp[mid] == search:
            return mid
        elif dp[mid] > search:
            end = mid - 1
        else:
            start = mid + 1

    return start

for i in range(1, n):
    if num_list[i] > dp[-1]:
        dp.append(num_list[i])
    else:
        idx = binary_search(num_list[i])
        dp[idx] = num_list[i]

print(len(dp))