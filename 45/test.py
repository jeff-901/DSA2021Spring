import unittest
import subprocess
import os
import sys


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

    def test_01_sample(self):
        self.run_testcase("sample1")

    def test_02_sample(self):
        self.run_testcase("sample2")

    def test_03_sample(self):
        self.run_testcase("sample3")

    def test_04_sample(self):
        self.run_testcase("sample4")

    def test_05_small(self):
        for i in range(48, 50):
            self.run_testcase(f"small{i}")


if __name__ == "__main__":
    unittest.main()
