n = int(input())
requests = []
for _ in range(n):
    a, t = map(int, input().split())
    requests.append((a, t))

start_times = []
current_time = 0
for a, t in requests:
    if a >= current_time:
        start_times.append(a)
        current_time = a + t
    else:
        start_times.append(current_time)
        current_time += t

for start_time in start_times:
    print(start_time)
