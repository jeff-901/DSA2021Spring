import os
import sys
import random


def generate(n):
    def _generate_tree(n, parent_idx, pos):
        if n == 0:
            return
        nodes.append([-1, -1])
        idx = len(nodes) - 1
        if parent_idx != -1:
            if pos == "left":
                nodes[parent_idx][0] = idx
            else:
                nodes[parent_idx][1] = idx
        if n == 1:
            return
        l = random.randint(0, n - 1)
        r = n - 1 - l
        left = _generate_tree(l, idx, "left")
        right = _generate_tree(r, idx, "right")
    MAX_KEY = 10 ** 9
    nodes = [(-1, -1)]
    keys = random.sample(range(1, MAX_KEY + 1), k=n)
    _generate_tree(n, -1, None)
    data = f"{n}\n" + \
        "".join([f"{keys[i]} {nodes[i+1][0]} {nodes[i+1][1]}\n" for i in range(n)])
    return data


def answer(input_data):
    def _search(idx, key):
        if idx == -1:
            return 0
        if data[idx][0] == key:
            return 1
        if data[idx][0] > key:
            return _search(data[idx][1], key)
        else:
            return _search(data[idx][2], key)
    data = [[int(x) for x in row.split()]
            for row in input_data.split("\n")[1:-1]]
    data = [None] + data
    ans = sum([_search(1, k) for k, _, _ in data[1:]])
    return f"{ans}\n"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} [name] [N_NODES]")
        sys.exit(1)

    name = sys.argv[1]
    N_NODES = int(sys.argv[2])

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

    input_data = generate(N_NODES)
    ans = answer(input_data)

    with open(input_path, "w") as fout:
        fout.write(input_data)

    with open(output_path, "w") as fout:
        fout.write(ans)
