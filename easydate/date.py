from datetime import datetime, timedelta
from forbiddenfruit import curse, curses


# better reachable now function
now = datetime.now

# int modifications
@curses(int, 'days')
@property
def int2days(self):
    return timedelta(days=self)

@curses(int, 'hours')
@property
def int2hours(self):
    return timedelta(hours=self)

@curses(int, 'minutes')
@property
def int2minutes(self):
    return timedelta(minutes=self)

@curses(int, 'seconds')
@property
def int2seconds(self):
    return timedelta(seconds=self)

# timedelta modifications
@curses(timedelta, 'after')
def after(self, dt):
    return dt + self

@curses(timedelta, 'before')
def before(self, dt):
    return dt - self

@curses(timedelta, 'from_now')
@property
def from_now(self):
    return now() + self

@curses(timedelta, 'ago')
@property
def ago(self):
    return now() - self
