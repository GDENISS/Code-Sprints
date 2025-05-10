
# def angryProfessor(k, a):
#     # Write your code here
#     return "YES"
def angryProfessor(k, a):
    on_time_count = 0
    for arrival in a:  # Bug: 'arrival_times' is undefined
        if arrival <= 0:
            on_time_count += 1
    return "YES" if on_time_count < k else "NO"
