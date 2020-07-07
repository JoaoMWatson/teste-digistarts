FILE = "sample.txt"


def read(file):
    operations = {
        '+' : lambda num1, num2: num1 + num2,
        '-' : lambda num1, num2: num1 - num2,
        '*' : lambda num1, num2: num1 * num2,
        '/' : lambda num1, num2: num1 / num2,
        '%' : lambda num1, num2: num1 % num2,
    }

    with open(file) as f:
        data = f.readlines()
        num1 = int(data[1], 2)
        num2 = int(data[2], 2)
        result = operations[data[0][0]](num1, num2)
        result = bin(result)[2:].zfill(8)
        print(result)

if __name__ == "__main__":
    read(FILE)
