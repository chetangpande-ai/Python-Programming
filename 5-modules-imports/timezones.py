class timezones:
    def __init__(self):
        self.timezone_list = ["UTC", "EST", "CST", "MST", "PST"]

    def display_timezones(self):
        for tz in self.timezone_list:
            print(tz)