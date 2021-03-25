#
# Testcases for DSA 37.
# Author: Jhan-Shuo Liu
#
# ========================================

import unittest
import subprocess
import random

# ========================================

random.seed()

def run(testcase, *args, which="our", input_data=None):
    if which == "our":
        script_name = testcase.our_script
    # elif which == "answer":
    #     script_name = testcase.answer_script
    else:
        raise ValueError(f"Invalid argument: {which}")
    return subprocess.run([script_name, *args],
                          capture_output=True, text=True,
                          timeout=testcase.timeout, input=input_data)

def ans_37(input_data=None):
    if (input_data == None):
        return
    lines = input_data.split("\n")
    n, q = lines.pop(0).split(" ")
    n = int(n)
    q = int(q)
    stdout=""
    num = []
    init = lines.pop(0).split(" ")
    for i in range(n):
        num.append(int(init[i]))
    print("init: ",num)
    for i in range(q):
        options = lines[i].split(" ")
        if options[0] == "Insert":
            num1 = int(options[1])
            num2 = int(options[2])
            num = num[:num1-1] + [num2] + num[num1-1:]
            # print(num)
        elif options[0] == "Delete":
            num1 = int(options[1])
            num.pop(num1-1)
            # print(num)
        elif options[0] == "Reverse":
            num1 = int(options[1])
            num2 = int(options[2])
            # print("Reverse: ", num1, num2)
            
            cut = num[num1-1:num2]
            cut.reverse()
            # print(cut)
            num = num[:num1-1].copy() + cut + num[num2:].copy()
            # print(num)
        else:
            num1 = int(options[1])
            num2 = int(options[2])
            num3 = int(options[3])
            sort = num[num1-1:num2]
            # print(num1, num2, len(sort))
            sort.sort()
            stdout+=f"{sort[num3-1]}\n"
    return stdout




def run_and_check(testcase, *args, input_data=None):
    ans = run(testcase, *args, which="our" ,input_data=input_data)
    # our = run(testcase, *args, which="our", input_data=input_data)
    # testcase.assertEqual(ans.returncode, our.returncode)
    testcase.assertEqual(ans.stdout, ans_37(input_data))
    # return ans


op = ["Insert", "Delete", "Reverse", "Query", "Query"]
def random_test_data(n, q):
    input_data=f"{n} {q}\n"
    for i in range(n):
        input_data+=f"{random.randint(-10**5, 10**5)} "
    input_data=input_data[:-1]
    input_data+="\n"
    # print(input_data)
    tot = n
    for i in range(q):
        ins = random.choice(op)
        if ins == "Insert":
            i = random.randint(1, tot + 1)
            input_data+=(f"{ins} {i} {random.randint(-10**5, 10**5)}\n")
            tot += 1
        elif ins == "Delete":
            i = random.randint(1, tot)
            input_data+=(f"{ins} {i}\n")
            tot -= 1
        elif ins == "Reverse":
            num1 = random.randint(1, n)
            num2 = random.randint(num1, n)
            input_data+=(f"{ins} {num1} {num2}\n")
        else:
            num1 = random.randint(1, n)
            num2 = random.randint(num1, n)
            num3 = random.randint(1, num2-num1+1)
            input_data+=(f"{ins} {num1} {num2} {num3}\n")
    return input_data

class TestTask(unittest.TestCase):
    def setUp(self):
        self.timeout = 8
        self.maxDiff = None
        self.our_script = "./36"

    def test_1_sample(self):
        our = run(self, input_data="5 5\n-10 1 4 -3 -5\nQuery 4 4 1\nQuery 1 2 1\nQuery 4 5 2\nQuery 2 3 2\nQuery 4 5 1\n")
        self.assertEqual(our.stdout, "-3\n-10\n-3\n4\n-5\n")
    
    def test_2_sample(self):
        our = run(self, input_data="5 5\n-2 4 4 -7 2\nDelete 5\nDelete 1\nInsert 2 6\nQuery 3 3 1\nQuery 4 4 1\n")
        self.assertEqual(our.stdout, "4\n-7\n")

    def test_3_sample(self):
        our = run(self, input_data="5 5\n-6 7 3 3 0\nReverse 1 4\nInsert 3 -6\nQuery 3 4 1\nReverse 4 5\nQuery 1 4 2\n" )
        self.assertEqual(our.stdout, "-6\n-6\n")

    def test_4_random_10_10(self):
        input_data = random_test_data(10, 10)
        run_and_check(self, input_data=input_data)


if __name__ == "__main__":
    unittest.main()
    # print(ans_37("5 5\n-6 7 3 3 0\nReverse 1 4\nInsert 3 -6\nQuery 3 4 1\nReverse 4 5\nQuery 1 4 2\n"))