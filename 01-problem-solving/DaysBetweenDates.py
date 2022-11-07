def is_leap(year):
    return year % 4 == 0


def days_in_month(year, month):
    months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if month == 2:
        if is_leap(year):
            return months[1] + 1
    return months[month - 1]


def is_same_month(year1, month1, year2, month2):
    return (year1 == year2) and (month1 == month2)


def get_days(year, month):
    return days_in_month(year, month)


def get_next_month(year, month):
    if month < 12:
        return year, month + 1
    else:
        return year + 1, 1


def is_date_before(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    else:
        if month1 < month2:
            return True
        else:
            return day1 < day2


def are_inputs_valid(year1, month1, day1, year2, month2, day2):
    return is_date_before(year1, month1, day1, year2, month2, day2)


def days_between_dates(year1, month1, day1, year2, month2, day2):
    if not are_inputs_valid(year1, month1, day1, year2, month2, day2):
        return None
    days = 0
    current_year, current_month = year1, month1
    while not is_same_month(current_year, current_month, year2, month2):
        days += get_days(current_year, current_month)
        current_year, current_month = get_next_month(current_year, current_month)
    days += (day2 - day1)
    return days


def get_date(date):
    return [int(x) for x in date.split('-')]


def main():
    date1 = input('Start day: dd-mm-yyyy: ')
    day1, month1, year1 = get_date(date1)
    date2 = input('Start day: dd-mm-yyyy: ')
    day2, month2, year2 = get_date(date2)

    print(f'Number of days between {date1} and {date2} is {days_between_dates(year1, month1, day1, year2, month2, day2)}')


if __name__ == '__main__':
    main()
