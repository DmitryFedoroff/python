def check_statement():
    bool_vals = range(2)
    for x in bool_vals:
        for y in bool_vals:
            for z in bool_vals:
                print(x, y, z, "-", (not (x or y or z) == ((not x) and (not y) and (not z))))
