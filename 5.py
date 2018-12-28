import unittest
import re


def prompt1():
    while True:
        nStr1 = input("What is the first number?\n")
        match1 = re.match(pattern, nStr1)
        if not match1:
            print("Please input a valid number.")
        elif match1.group(1):
            return float(nStr1)
        else:
            return int(nStr1)


def prompt2():
    while True:
        nStr2 = input("What is the second number?\n")
        match2 = re.match(pattern, nStr2)
        if not match2:
            print("Please input a valid number.")
        elif match2.group(1):
            return float(nStr2)
        else:
            return int(nStr2)


def printResult(n1, n2):
    print("""{0} + {1} = {2}
{0} - {1} = {3}
{0} * {1} = {4}
{0} / {1} = {5}""".format(n1, n2, n1+n2, n1-n2, n1*n2,
                          n1/n2 if n2 != 0 else "undefined"))


def parseTestFunction(nStr):
    match = re.match(pattern, nStr)
    if not match:
        return False
    elif match.group(1):
        return float(nStr)
    else:
        return int(nStr)


class TestParse(unittest.TestCase):
    inputStrings = ["0123", "-12", "12.1", "asd", "12.", "013.10", ""]
    expectation = [123, False, 12.1, False, False, 13.1, False]

    def test_parseNumber(self):
        for n, e in zip(TestParse.inputStrings, TestParse.expectation):
            with self.subTest(input=n, expectedResult=e):
                self.assertEqual(parseTestFunction(n), e)


if __name__ == "__main__":
    test = False

    # non-negative number pattern
    pattern = re.compile(r"^\d+(\.\d+)?$")

    if test:
        unittest.main()
    else:
        n1 = prompt1()
        n2 = prompt2()
        printResult(n1, n2)
