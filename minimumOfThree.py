tries = int(input())
answer = []
for x in range(tries):
    values = input().split()
    ans = map(int, values)
    answer = sorted(ans)
    print(answer[0])
