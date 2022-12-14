def read_input():
    with open('input.txt', 'r') as file:
        _input = file.readline()
        return _input


def write_output(data):
    with open('output.txt', 'w') as file:
        file.write(data)


def reverse_string_rec(string):
    if string == "":
        return string

    return string[-1] + reverse_string_rec(string[:-1])


if __name__ == "__main__":
    string = read_input()

    reversed_string = reverse_string_rec(string)
    write_output(reversed_string)
