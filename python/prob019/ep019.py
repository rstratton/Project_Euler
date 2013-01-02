dotw = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
month_lens = {"jan":31, "feb":28, "mar":31, "apr":30, "may":31, "jun":30, \
          "jul":31, "aug":31, "sep":30, "oct":31, "nov":30, "dec":31}
months = month_lens.keys()
is_leap = {}
for i in range(1901,2001):
    if i % 4 == 0:
        is_leap[i] = True
    else:
        is_leap[i] = False
years = is_leap.keys()
num_days = 0
for key in is_leap.keys():
    if is_leap[key] == True:
        num_days += 366
    else:
        num_days += 365
dates = {}
jan_1_1901 = "tue"

