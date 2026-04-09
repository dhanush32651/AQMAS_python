def validate(value):
    try:
        v = float(value)
        if v < 0:
            raise ValueError
        return v
    except:
        print("Invalid input")
        return None