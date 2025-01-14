def printer_error(s):
    valid_chars = 'abcdefghijklm'
    errors = 0
    for char in s:
        if char not in valid_chars:
            errors += 1
    return f"{errors} / {len(s)}"
print(printer_error("aaaxbbbbyyhwawiwjjjwwm"))

