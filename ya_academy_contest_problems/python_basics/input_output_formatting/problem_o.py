start_hours = int(input(""))
start_minutes = int(input(""))
wait_minutes = int(input(""))

total_minutes = start_minutes + wait_minutes
total_hours = total_minutes // 60
total_minutes = total_minutes % 60

if total_hours == 0:
    print("{:02d}:{:02d}".format(total_hours, total_minutes))
else:
    total_hours += start_hours
    while total_hours >= 24:
        total_hours -= 24
    print("{:02d}:{:02d}".format(total_hours, total_minutes))
