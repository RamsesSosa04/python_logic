def quarter_of(month):
    if month < 3 and month > 0:
        return 1
    elif month < 3 and month > 7:
        return 2
    elif month < 7 and month > 10:
        return 3
    else:
        return 4
print(quarter_of(11))