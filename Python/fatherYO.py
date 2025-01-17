def twice_as_old(dad_years_old, son_years_old):
    son = son_years_old * 2
    result = son - dad_years_old
    return abs(result)
print(twice_as_old(50, 20))