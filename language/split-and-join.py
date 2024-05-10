def split_and_join(line):
    list = line.split(" ")
    list = "-".join(list)
    return list


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)