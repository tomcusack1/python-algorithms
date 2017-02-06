def convert_to_hours(hours=0, minutes=0, seconds=0):
    """Time function to represent h:m:s time data as a single hour decimal

    Args:
        hours (int): The largest time unit for our function. 24 hours in a day.
        minutes (int): A time unit. 60 minutes in an hour.
        seconds (int): A time unit. 60 seconds in an hour.

    Returns:
        (float) For example: 1h, 1m, 0s would return 1.016

    """
    return hours + (float(minutes) / 60.0) + (float(seconds) / 3600.0)

print convert_to_hours(1, 1, 0)  # Prints 1.01666666667
