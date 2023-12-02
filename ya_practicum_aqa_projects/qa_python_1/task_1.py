STRING = "1h 45m,360s,25m,30m 120s,2h 60s"
values_of_string = STRING.replace(" ", "").split(",")
minutes_counter = 0

for value in values_of_string:
    if "h" in value:
        minutes_counter += int(value.split("h")[0]) * 60
        if "m" in value:
            minutes_counter += int((value.split("h"))[1].replace("m", ""))
        elif "s" in value:
            minutes_counter += int((value.split("h"))[1].replace("s", "")) // 60
    elif "m" in value:
        minutes_counter += int(value.split("m")[0])
        if "s" in value:
            minutes_counter += int((value.split("m"))[1].replace("s", "")) // 60
    elif "s" in value:
        minutes_counter += int(value.split("s")[0]) // 60

print(minutes_counter)
