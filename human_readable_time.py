def make_readable(seconds):
    if seconds > 359999:
        seconds = 359999

    hour = seconds//3600
    minute = (seconds-hour*3600)//60
    second = seconds-hour*3600-minute*60

    return f"{hour:02d}:{minute:02d}:{second:02d}"

print(make_readable(359999)) #, "00:00:00")