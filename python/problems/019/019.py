#!/usr/bin/env python2

from itertools import cycle, takewhile

JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC = range(12)
MON, TUE, WED, THU, FRI, SAT, SUN = range(7)

class Iter(object):
    def __iter__(self):
        return self


class IntIter(Iter):
    def __init__(self, start):
        self.current = start

    def next(self):
        self.current += 1
        return self.current


class IntCycleIter(Iter):
    def __init__(self, start, cycle_len):
        self.current = start
        self.iterator = cycle(xrange(cycle_len))
        while self.current != next(self.iterator): pass

    def next(self):
        self.current = next(self.iterator)
        return self.current


class DayOfTheWeekIter(IntCycleIter):
    def __init__(self, start_dotw):
        super(DayOfTheWeekIter, self).__init__(start_dotw, 7)


class MonthIter(IntCycleIter):
    def __init__(self, start_month):
        super(MonthIter, self).__init__(start_month, 12)


class YearIter(IntIter):
    def __init__(self, start_year):
        super(YearIter, self).__init__(start_year)


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0

def num_days_in_month(month, year):
    if month in (SEP, APR, JUN, NOV):
        return 30
    elif month == FEB:
        return 29 if is_leap_year(year) else 28
    else:
        return 31

class Day(object):
    def __init__(self, date, month, year, dotw):
        self.date = date
        self.month = month
        self.year = year
        self.dotw = dotw

    @classmethod
    def copy(self, other):
        return Day(other.date,
                   other.month,
                   other.year,
                   other.dotw)

    def __eq__(self, other):
        return self.date == other.date and \
               self.month == other.month and \
               self.year == other.year

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "{0}, {1} {2}, {3}".format(self.dotw,
                                          self.month,
                                          self.date,
                                          self.year)


class DaysIter(Iter):
    def __init__(self, start_day):
        self.current = start_day
        self.days_in_month = num_days_in_month(start_day.month, start_day.year)
        # Create iterators
        self.year_iter = YearIter(start_day.year)
        self.dotw_iter = DayOfTheWeekIter(start_day.dotw)
        self.month_iter = MonthIter(start_day.month)

    def next(self):
        result = self.current

        next_day = Day.copy(self.current)
        if self.current.date == self.days_in_month:
            if self.current.month == DEC:
                next_day.year = next(self.year_iter)
            next_day.date = 1
            next_day.month = next(self.month_iter)
            self.days_in_month = num_days_in_month(next_day.month, next_day.year)
        else:
            next_day.date += 1
        next_day.dotw = next(self.dotw_iter)

        self.current = next_day
        return result


def main():
    # Start at known date/day-of-the-week combination
    days = DaysIter(Day(1, JAN, 1900, MON))

    # Consume days up until we want to start counting Sundays (we start
    # counting Sundays at January 1st, 1901)
    while next(days) != Day(31, DEC, 1900, 0): pass

    # Construct iterator which stops iteration after the days it returns have
    # passed the 20th century mark
    def is_not_last_day(day):
        return day != Day(31, DEC, 2000, 0)
    twentieth_century = takewhile(is_not_last_day, days)

    # Count the number of Sundays which are also the 1st of the month
    def is_sunday_first(day):
        return day.date == 1 and day.dotw == SUN
    sunday_firsts = [day for day in twentieth_century if is_sunday_first(day)]

    print len(sunday_firsts)


if __name__ == "__main__":
    main()
