import unittest
import subprocess
import os
import sys

import generate


class Test(unittest.TestCase):
    def setUp(self):
        self.timeout = 3
        self.maxDiff = None
        self.script_name = os.path.join(".", "bin", os.listdir("./bin")[0])

    def run_testcase(self, name):
        with open(os.path.join("input", f"{name}.txt")) as fin:
            input_data = fin.read()
        with open(os.path.join("output", f"{name}.txt")) as fin:
            ans = fin.read()
        output = subprocess.check_output([self.script_name], text=True,
                                         timeout=self.timeout, input=input_data)
        self.assertEqual(output, ans)

    def test_01_sample1(self):
        self.run_testcase("sample1")

    def test_02_sample1(self):
        self.run_testcase("sample2")

    def test_03_sample1(self):
        self.run_testcase("sample3")

    def test_04_random(self):
        for i in range(1000):
            input_data = generate.generate()
            ans = generate.answer(input_data)
            output = subprocess.check_output([self.script_name], text=True,
                                             timeout=self.timeout, input=input_data)
            self.assertEqual(output, ans)

    def test_05(self):
        L = list()
        s = "0" * (10 ** 5 - 1) + "1"
        input_data = f"1\n{s}\nx\n"
        ans = generate.answer(input_data)
        output = subprocess.check_output([self.script_name], text=True,
                                         timeout=self.timeout, input=input_data)
        self.assertEqual(output, ans)

    def test_06(self):
        L = list()
        s = "01" * (10 ** 5 // 2)
        input_data = f"1\n{s}\nx\n"
        ans = generate.answer(input_data)
        output = subprocess.check_output([self.script_name], text=True,
                                         timeout=self.timeout, input=input_data)
        self.assertEqual(output, ans)


if __name__ == "__main__":
    unittest.main()
