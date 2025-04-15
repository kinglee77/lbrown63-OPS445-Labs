#!/usr/bin/env python3
# Student ID: lbrown63

class Time:
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def valid_time(self):
        return 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60

    def time_to_sec(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def change_time(self, seconds):
        total = self.time_to_sec() + seconds
        nt = sec_to_time(total)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second

    def sum_times(self, t2):
        total = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total)

def sec_to_time(seconds):
    t = Time()
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60)
    return t
