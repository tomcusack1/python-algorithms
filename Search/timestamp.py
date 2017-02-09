import unittest


def convert_to_hours(hours: int, minutes: int, seconds: int) -> float:
    """Represents h:m:s time data as an individual floating point decimal in hours

    Args:
        hours (int): The largest time unit for our function. 24 hours in a day.
        minutes (int): A time unit. 60 minutes in an hour.
        seconds (int): A time unit. 60 seconds in an hour.

    Return: (float) For example: 1h, 1m, 0s would return 1.016.
    """
    return float(hours) + (float(minutes) / 60.0) + (float(seconds) / 3600.0)


class TestTime(unittest.TestCase):
    def test_one(self):
        # 1 hour 30 minutes --> 1.5 hours
        self.assertEqual(convert_to_hours(1, 30, 0), 1.5)

    def test_two(self):
        # 72,000 seconds    --> 20 hours
        self.assertEqual(convert_to_hours(0, 0, 72000), 20)

    def test_three(self):
        # 60,000 minutes    --> 1000 hours
        self.assertEqual(convert_to_hours(0, 60000, 0), 1000)

if __name__ == '__main__':
    unittest.main()
