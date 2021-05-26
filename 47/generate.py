import os
import sys
import random

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def generate():
    T = random.randint(100, 100)
    input_data = f"{T}\n"
    for i in range(T):
        for j in range(random.randint(800, 1000)):
            input_data += random.choice(characters)
        input_data += "\n"

        for j in range(random.randint(3, 7)):
            input_data += random.choice(characters)
        input_data += "\n"
    return input_data


def check_match(ans, cur):
    # print(ans)
    # print(cur)
    for key in ans:
        if ans[key] > cur[key]:
            return False
    return True


def answer(input_data):
    data = input_data.split("\n")
    T = int(data[0])
    output_data = ""
    for i in range(T):
        D = data[2 * i + 1]
        P = data[2 * i + 2]
        p_cnt = {}
        for ele in P:
            if ele in p_cnt:
                p_cnt[ele] += 1
            else:
                p_cnt[ele] = 1
        left = 0
        right = 1
        min_ = 10 ** 6
        best_left = -1
        best_right = -1
        d_cnt = {}
        for ele in characters:
            d_cnt[ele] = 0
        d_cnt[D[left]] = 1


        while right < len(D):
            d_cnt[D[right]] += 1
            if check_match(p_cnt, d_cnt):
                d_cnt[D[left]] -= 1
                left += 1
                while check_match(p_cnt, d_cnt):
                    d_cnt[D[left]] -= 1
                    left += 1
                l = right - left + 2
                if min_ > l:
                    best_left = left - 1
                    best_right = right
                    min_ = l
                right += 1
            else:
                right += 1
        if best_left != -1:
            E = D[:best_left] + D[best_right + 1 :]
        else:
            E = D
        D = E[:]
        s = 0
        e = len(D)
        n = 1
        front = ""
        back = ""
        while s + n <= e - n:
            if D[s : s + n] == D[e - n : e]:
                front += D[s : s + n] + "|"
                back = "|" + D[e - n : e] + back
                s = s + n
                e = e - n
                n = 1
            else:
                n += 1
        if s < e:
            front += D[s:e]
        output_data += front + back + "\n"
    return output_data

    return str(sum([int(x) for x in input_data.split()]))


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
