n = int(input())
ans = 0
for i in range(n):
    l, c = map(int, input().split())
    if l > c:
        ans += c
    else:
        continue
print(ans)