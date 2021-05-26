import os
import sys
import random


def generate():
    L = list()
    n = random.randint(8, 12)
    for _ in range(n):
        L.append(str(random.randint(0, 1)))
    s = "".join(L)
    return f"1\n{s}\nx\n"


def answer(input_data):
    s = input_data.split("\n")[1]
    front = list()
    back = list()
    while s:
        should_break = True
        for i in range(1, len(s) // 2 + 1):
            if s[:i] == s[-i:]:
                front.append(s[:i])
                back.append(s[:i])
                s = s[i:-i]
                should_break = False
                break
        if should_break:
            front.append(s)
            break
    back.reverse()
    return "|".join(front + back) + "\n"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} [name]")
        sys.exit(1)

    name = sys.argv[1]

    input_dir = "input"
    output_dir = "output"
    if not os.path.exists(input_dir):
        os.mkdir(input_dir)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    input_path = os.path.join(input_dir, f"{name}.txt")
    output_path = os.path.join(output_dir, f"{name}.txt")

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
