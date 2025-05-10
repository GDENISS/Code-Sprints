def angryProfessor(k, a):
    on_time_count = 0
    for arrival in a:  # Bug: 'arrival_times' is undefined
        if arrival <= 0:
            on_time_count += 1
    return "YES" if on_time_count < k else "NO"

k = 3
a = [-1, -3, 4, 2]

print(angryProfessor(k, a))