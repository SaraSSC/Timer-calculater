def week_dias(weekname: str, dias: int) -> str:
    week = [
        "sunday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
    ]
    while dias > 7:
        dias -= 7
    pos = week.index(weekname.lower())
    index = pos + dias
    while index >= 7:
        index -= 7
    return week[index].title()


def add_time(start, duration, week=None):
    start, alturadodia = start.split(" ")
    hour, minute = [int(x) for x in start.split(":")]
    dhour, dminute = [int(x) for x in duration.split(":")]
    minute += dminute
    hour += dhour
    days = 0
    while True:
        if minute >= 60:
            hour += 1
            minute -= 60
        if hour > 12:
            if alturadodia == "PM":
                days += 1
                alturadodia = "AM"
            else:
                alturadodia = "PM"
            hour -= 12
        if minute < 60 and hour <= 12:
            if hour == 12 and minute > 0:
                alturadodia = "AM" if alturadodia == "PM" else "PM"
                if alturadodia == "AM": days += 1
            break
    new_time = "{}:{:02d} {}".format(hour, minute, alturadodia)
    if week is not None:
        new_time += ", {}".format(week_dias(week, days))
    if days > 0:
        if days == 1:
            new_time += " (next day)"
        else:
            new_time += f" ({days} days later)"

    return new_time
