#
# Testcases for DSA 40.
# Author: Jhan-Shuo Liu
#
# ========================================

import unittest
import subprocess
import random

# ========================================

random.seed(0)

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

def ans_36(input_data=None):
    if (input_data == None):
        return
    lines = input_data.split("\n")
    n, m = lines.pop(0).split(" ")
    n = int(n)
    m = int(m)
    ans = [[] for _ in range(n)]
    for i in range(m):
        options = lines[i].split(" ")
        if options[0] == "enter":
            # num1 = int(options[1])
            ans[int(options[1])].append(options[2])
        elif options[0] == "leave":
            if (len(ans[int(options[1])]) > 0):
                ans[int(options[1])].pop()
        else:
            # if (len(ans[int(options[1])]) > 0):
            while len(ans[int(options[1])]) > 0:
                ans[int(options[2])].append(ans[int(options[1])].pop())
    stdout = ""
    for i in range(n):
        stdout += " ".join(ans[i])
        stdout += "\n"
    return stdout




def run_and_check(testcase, *args, input_data=None):
    ans = run(testcase, *args, which="our" ,input_data=input_data)
    # our = run(testcase, *args, which="our", input_data=input_data)
    # testcase.assertEqual(ans.returncode, our.returncode)
    testcase.assertEqual(ans.stdout, ans_36(input_data))
    # return ans


op = ["leave", "migrate", "enter"]
def random_test_data(k, n):
    input_data=f"{k} {n}\n"
    for i in range(n):
        ins = random.choice(op)
        if ins == "leave":
            num = random.randint(0, k-1)
            input_data+=(f"{ins} {num}\n")
        elif ins == "enter":
            num1 = random.randint(0, k-1)
            num2 = random.randint(1, 10**4-1)
            input_data+=(f"{ins} {num1} {num2}\n")
        else:
            num1 = random.randint(0, k-1)
            num2 = random.randint(0, k-1)
            while ( num2 == num1):
                num2 = random.randint(0, k-1)
            input_data+=(f"{ins} {num1} {num2}\n")
    return input_data

class TestTask(unittest.TestCase):
    def setUp(self):
        self.timeout = 1
        self.maxDiff = None
        self.our_script = "./36"

    def test_1_sample(self):
        run_and_check(self, input_data="3 7\nenter 1 1\nenter 1 2\nenter 2 3\nenter 2 4\nenter 2 5\nleave 2\nmigrate 2 1\n")
    
    def test_2_sample(self):
        run_and_check(self, input_data="5 30\nenter 4 2788\nleave 4\nmigrate 4 3\nenter 2 132\nenter 0 2800\nmigrate 2 3\nenter 1 3116\nenter 3 8714\nenter 0 267\nmigrate 0 1\nenter 4 4055\nmigrate 3 0\nenter 2 2567\nmigrate 1 4\nmigrate 1 2\nenter 4 72\nleave 1\nmigrate 0 4\nmigrate 4 1\nmigrate 2 0\nenter 1 1230\nmigrate 3 2\nmigrate 0 4\nleave 3\nenter 2 8548\nenter 0 4983\nleave 4\nmigrate 3 2\nenter 3 3731\nenter 1 9536\n"        )
    
    def test_3_random_10_100(self):
        input_data = random_test_data(10, 100)
        run_and_check(self, input_data=input_data)

    def test_4_random_1000_1000000(self):
        input_data = random_test_data(1000, 1000000)
        run_and_check(self, input_data=input_data)


if __name__ == "__main__":
    unittest.main()