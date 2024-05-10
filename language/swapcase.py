def swap_case(s):
    new_string = str()
    for c in s:
        if c.isupper():
            new_string += c.lower()
        elif c.islower():
            new_string += c.upper()
        else:
            new_string += c
    return new_string


if __name__ == '__main__':
    swap_case("Www.HackerRank.com")
