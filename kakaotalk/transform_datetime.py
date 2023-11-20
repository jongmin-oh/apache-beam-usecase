import datetime


def datetime_to_int(kakao_datetime):
    def check_night(x):
        return 1 if ("오후" in x and "12:" not in x) else 0

    def check_midnight(x):
        return 1 if ("오전" in x and "12:" in x) else 0

    is_night = check_night(kakao_datetime)
    is_midnight = check_midnight(kakao_datetime)

    split_datetime = kakao_datetime.split()

    year = split_datetime[0][:-1]
    month = split_datetime[1][:-1]
    day = split_datetime[2][:-1]
    hour = split_datetime[4][: split_datetime[4].find(":")]
    minute = split_datetime[4][split_datetime[4].find(":") + 1:]

    if is_night:
        hour = str(int(hour) + 12)
    elif is_midnight:
        hour = "00"
    return datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))


if __name__ == "__main__":
    text = "2019년 12월 31일 오후 11:59"
    print(type(datetime_to_int(text)))
    print(datetime_to_int(text))
