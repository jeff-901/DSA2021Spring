import os
import sys
import random


def generate():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return f"{a} {b}\n"


def answer(input_data):
    return str(sum([int(x) for x in input_data.split()]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} [name]")
        sys.exit(1)

    name = sys.argv[1]
    input_path = os.path.join("input", f"{name}.txt")
    output_path = os.path.join("output", f"{name}.txt")

    if os.path.exists(input_path):
        print(f"The file {input_path} already exists!")
        sys.exit(1)
    if os.path.exists(output_path):
        print(f"The file {output_path} already exists!")
        sys.exit(1)

    input_data = generate()
    ans = answer(input_data)

    with open(input_path, "w") as fout:
        fout.write(input_data)

    with open(output_path, "w") as fout:
        fout.write(ans)
