def fake_bin(x):
    result = ""
    for digit in x:
        if int(digit) < 5:
            result += "0"
        else:
            result += "1"
    return result

x = "941397315975486433143425066"
result = fake_bin(x)
print(result)
