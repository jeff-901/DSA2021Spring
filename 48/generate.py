import os
import sys
import random


def generate():
    n = 5
    q = 5
    input_data = f"{n} {q}\n"
    ans = list()
    L = list()
    for _ in range(n):
        L.append(random.randint(-n, n))
    input_data += " ".join([str(x) for x in L]) + "\n"
    for _ in range(q):
        op = random.choice([1, 2, 4])
        if op == 1:
            p = random.randint(-n, n)
            k = random.randint(0, len(L))
            input_data += f"1 {p} {k}\n"
            L.insert(k, p)
        elif op == 2:
            k = random.randint(1, len(L))
            input_data += f"2 {k}\n"
            L.pop(k-1)
        elif op == 4:
            l = random.randint(1, len(L))
            r = random.randint(1, len(L))
            if (l > r):
                (l, r) = (r, l)
            input_data += f"4 {l} {r}\n"
            ans.append(str(max(L[l-1:r])))
        else:
            pass
    ans = "\n".join(ans) + "\n" if ans else ""
    return input_data, ans


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

    input_data, ans = generate()

    with open(input_path, "w") as fout:
        fout.write(input_data)

    with open(output_path, "w") as fout:
        fout.write(ans)
