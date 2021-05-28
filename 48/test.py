import unittest
import subprocess
import os
import sys

from generate import generate


class Test(unittest.TestCase):
    def setUp(self):
        self.timeout = 1
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

    def test_02_sample2(self):
        self.run_testcase("sample2")

    def test_03_sample3(self):
        self.run_testcase("sample3")

    def test_04(self):
        for _ in range(100):
            input_data, ans = generate()
            output = subprocess.check_output([self.script_name], text=True,
                                             timeout=self.timeout, input=input_data)
            self.assertEqual(output, ans, [input_data])


if __name__ == "__main__":
    unittest.main()
