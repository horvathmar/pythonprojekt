def beker(kerdes, max=2):
    while True:
        try:
            value = int(input(kerdes))
            if 1 <= value <= max:
                return value    
        except ValueError:
            pass