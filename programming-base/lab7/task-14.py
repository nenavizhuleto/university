def read_input():
    with open('input.txt', 'r') as file:
        _input = file.readline()
        return _input


def write_output(data):
    with open('output.txt', 'w') as file:
        file.write(data)


def balanced(s, brackets=['()', '[]', '{}', '<>']):
    if len(s.strip()) % 2 != 0:
        return 'NO'
    if s.strip() == '':
        return 'YES'
    
    tmp = s
    for bracket in brackets:
        tmp = tmp.replace(bracket, '')

    if tmp == s:
        return 'NO'

    return balanced(tmp, brackets)

if __name__ == '__main__':
    inp = read_input() 
    result = balanced(inp)
    print(result)
    write_output(result)
