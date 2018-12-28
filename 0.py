import unittest
import re
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


def askBill():
    while True:
        billAmount = input("What is the bill amount in dollars?\n")
        billMatch = billPattern.fullmatch(billAmount)
        if not billMatch:
            print("\nPlease enter a valid bill amount.")
        else:
            return float(billMatch.group(1))


def askTip():
    while True:
        tipRate = input("\nWhat is the tip rate in percentage?\n")
        tipMatch = tipPattern.fullmatch(tipRate)
        if not tipMatch:
            print("\nPlease enter a valid tip amount.")
        else:
            return float(tipMatch.group(1))


def printResult(billAmount, tipRate):
    tip = round(billAmount*(tipRate/100), 2)
    total = billAmount+tip
    print("\n\nTip: $", tip, "\nTotal: $", total)


def testParseBill(billAmountString):
    return bool(billPattern.fullmatch(billAmountString))


def testParseTip(tipRateString):
    return bool(tipPattern.fullmatch(tipRateString))


class TestInput(unittest.TestCase):

    billInputs = ["", "1asd2.3fg", "12345", "012345", "123.",
                  "123.", "123.0", "123.45", "123.456", "$123",
                  "$123.00", "123$", "123.00$", " $$ 123$ $", " $123.00 $$"]

    billResults = [False, False, True, False, False,
                   False, False, True, False, True,
                   True, True, True, True, True]

    tipInputs = ["", "1asd2.3fg", "12345", "123.", "123.0",
                 "123.1", "123.10", "%123", "%123.00", "123%",
                 "123.00%", " % %%  %   123 % %% %", " % %%  %   123.00 % %% %", " % %%  %   123.01 % %% %"]

    tipResults = [False, False, True, False, False,
                  True, False, True, False, True,
                  False, True, False, True]

    def test_bill(self):
        for billInput, billResult in zip(TestInput.billInputs, TestInput.billResults):
            with self.subTest(bill=billInput, expectedResult=billResult):
                self.assertEqual(testParseBill(billInput), billResult)

    def test_tip(self):
        for tipInput, tipResult in zip(TestInput.tipInputs, TestInput.tipResults):
            with self.subTest(tip=tipInput, expectedResult=tipResult):
                self.assertEqual(testParseTip(tipInput), tipResult)


if __name__ == "__main__":
    test = False

    billPattern = re.compile(r'[ \$]*([1-9]\d*(\.\d\d)?)[ \$]*')
    tipPattern = re.compile(r'[ %]*([1-9]\d*(\.\d*[1-9])?)[ %]*')

    if not test:
        bill = askBill()
        tip = askTip()
        printResult(bill, tip)
    else:
        unittest.main()


# GUI Implementation???
