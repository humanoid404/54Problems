import re
import unittest


def promptMetric():
    while True:
        metricStr = input("Choose your metric: [1] feet, [2] meters\n")

        if not re.fullmatch(patternMetric, metricStr):
            print("\nPlease input either 1 or 2.")
        elif metricStr.lower() in ["1", "[1]", "feet", "foot", "imperial", "imperial system", "imperial metric", "imperial metric system"]:
            return "feet"
        elif metricStr.lower() in ["2", "[2]", "meter", "meters", "metric", "metric system"]:
            return "meters"
        else:
            print("\nPlease input either 1 or 2.")


def promptLength(metric):
    while True:
        length = input("What is the length of the room in {0}?\n".format(metric))

        if not re.fullmatch(patternNumber, length):
            print("\nPlease enter a valid number.")
        else:
            return float(length)


def promptWidth(metric):
    while True:
        width = input("What is the width of the room in {0}?\n".format(metric))

        if not re.fullmatch(patternNumber, width):
            print("\nPlease enter a valid number.")
        else:
            return float(width)


def promptResult(metric, length, width):
    constant = 0.3048  # 1 foot = constant * 1 meter
    print("\nYou entered dimensions of {1} {0} by {2} {0}.".format(metric, length, width))
    if metric == "feet":
        feetMetersPair = (length*width, length*width*constant**2)
    else:  # metric == "meters"
        feetMetersPair = (length*width/constant**2, length*width)
    feetMetersPair = map(lambda x: round(x, 5), feetMetersPair)  # round to 4 digits
    print("The area is {0} square feet, or equivalently, {1} square meters".format(*feetMetersPair))


def metricParseTest(metricStr):
    if not re.fullmatch(patternMetric, metricStr):
        return 0
    elif metricStr.lower() in ["1", "[1]", "feet", "foot", "imperial", "imperial system", "imperial metric", "imperial metric system"]:
        return 1
    elif metricStr.lower() in ["2", "[2]", "meter", "meters", "metric", "metric system"]:
        return 2
    else:
        return 3


def numberParseTest(numberStr):
    if not re.fullmatch(patternNumber, numberStr):
        return 0
    else:
        return 1


class TestMetricParse(unittest.TestCase):
    metricInputs = ["1", "[1]", "feet", "foot", "imperial", "imperial system", "imperial metric", "imperial metric system",
                    "2", "[2]", "meter", "meters", "metric", "metric system",
                    "Foot", "imperial Metric system", "METERS",
                    "asd", "0", "", "system"]
    metricExpectations = [1]*8 + [2]*6 + [1, 1, 2] + [0]*4

    numberInputs = ["", "12.", ".23", "."] + ["12.2", "0.0", "010", "01.10"]
    numberExpectations = [0]*4 + [1]*4

    def test_metricParse(self):
        for m, e in zip(TestMetricParse.metricInputs, TestMetricParse.metricExpectations):
            with self.subTest(metricInput=m, expectedResult=e):
                self.assertEqual(metricParseTest(m), e)

    def test_numberParse(self):
        for n, e in zip(TestMetricParse.numberInputs, TestMetricParse.numberExpectations):
            with self.subTest(numberInput=n, expectedResult=e):
                self.assertEqual(numberParseTest(n), e)


if __name__ == "__main__":
    test = False

    patternMetric = re.compile(r"(?i)[12]|\[[12]\]|feet|foot|meter|meters|imperial( metric)?( system)?|metric( system)?")
    patternNumber = re.compile(r"\d+(\.\d+)?")

    if test:
        unittest.main()
    else:
        metric = promptMetric()
        length = promptLength(metric)
        width = promptWidth(metric)
        promptResult(metric, length, width)
