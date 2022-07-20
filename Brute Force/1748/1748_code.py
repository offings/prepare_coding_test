n = int(input())
answer = 0

prev = 0
next = 9
while True:
    if n <= next:
        answer += len(str(next)) * (n - prev)
        print(answer)
        break
    else:
        answer += len(str(next)) * (next - prev)
        prev = prev * 10 + 9
        next = next * 10 + 9