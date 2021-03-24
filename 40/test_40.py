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
    elif which == "answer":
        script_name = testcase.answer_script
    else:
        raise ValueError(f"Invalid argument: {which}")
    return subprocess.run([script_name, *args],
                          capture_output=True, text=True,
                          timeout=testcase.timeout, input=input_data)

def run_and_check(testcase, *args, input_data=None, ans=None):
    our = run(testcase, *args, which="our", input_data=input_data)
    for our_ans, test in zip(our.stdout.strip().split("\n"), input_data.strip().split("\n")):
        our_ans = float(our_ans)
        ans = run(testcase, "-c", f"print({test})", which="answer")
        ans_ans = float(ans.stdout)
        testcase.assertEqual(abs(our_ans - ans_ans) < max(1, ans_ans), True)

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
        self.our_script = "./40"
        self.answer_script = "python3"

    def test_1_sample(self):
        run_and_check(self, input_data="3\n3+1-2\n")
    
    def test_2_sample(self):
        run_and_check(self, input_data="1+2*3\n1-2*3")
    
    def test_3_sample(self):
        run_and_check(self, input_data="(1+2)*3")

    # def test_4_random_1000_1000000(self):
    #     input_data = random_test_data(1000, 1000000)
    #     run_and_check(self, input_data=input_data)


if __name__ == "__main__":
    unittest.main()