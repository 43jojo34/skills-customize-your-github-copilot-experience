def is_even(number):
    return number % 2 == 0


def format_name(first_name, last_name):
    return f"{first_name.strip().title()} {last_name.strip().title()}"


def calculate_total(values):
    return sum(values)