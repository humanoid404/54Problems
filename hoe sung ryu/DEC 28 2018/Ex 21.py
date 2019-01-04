class monthswitch:
    def number(self, arg):
        self.month_number = "month_" + str(arg)
        self.number = getattr(self, self.month_number, lambda: "default")
        return self.number()

    def month_1(self):
        month = "January"
        return month

    def month_2(self):
        month = "Feburary"
        return month

    def month_3(self):
        month = "March"
        return month

    def month_4(self):
        month = "April"
        return month

    def case_default(self):
        print("default")


num = int(input("Please enter the number of the month"))
m = monthswitch()

# single output
print("The name of the month is {0}".format(m.number(num)))

#2. challenges

class monthswitch:
    def number(self, nation, arg):
        self.month_nation_number = "month_" + str(nation)+"_"+str(arg)
        self.number = getattr(self, self.month_nation_number, lambda: "default")
        return self.number()

    def month_eng_1(self):
        month ="January"
        return month

    def month_kor_1(self):
        month="일 월"
        return month
    def case_default(self):
        print("default")


num = int(input("Please enter the number of the month"))
nation=str(input("Nation"))
m = monthswitch()

# single output
print("The name of the month is {0}".format(m.number(nation,num)))
