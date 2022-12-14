import test

def read_input():
    with open('input.txt', 'r') as file:
        _input = file.readline()
        return _input


def write_output(data):
    with open('output.txt', 'w') as file:
        file.write(data)

if __name__ == "__main__":
    n = int(input("Enter size of an array: "))
    print(f"Testing {n} sized array. Wait until done...")

    [results, arrays] = test.test(n)
    results = f"Number of elements: {n}\n\n" + results
    write_output(results)
