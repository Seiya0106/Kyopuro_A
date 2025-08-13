N, S = map(int, input().split())
T = list(map(int, input().split()))

if T[0] > S:
  print("No")
  exit()
for i in range(1, len(T)):
  if T[i] - T[i - 1] > S:
    print("No")
    exit()
print("Yes")
