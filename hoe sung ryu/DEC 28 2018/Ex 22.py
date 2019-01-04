#Ex 22 comparing Numbers

#1.General

first=float(input("Enter the first number"))
second=float(input("Enter the second number"))
third=float(input("Enter the third number"))

list=[]
list.append(first)
list.append(second)
list.append(third)


if list[0] > list[1]:
    tem=list[0]
    list[0]=list[1]
    list[1]=tem
else:
    if list[1] > list[2]:
        tem = list[1]
        list[1] = list[2]
        list[2] = tem
    else:
        pass



print("The largest number is {number}".format(number=list[2]))



#2. challenges

first=float(input("Enter the first number"))
second=float(input("Enter the second number"))
third=float(input("Enter the third number"))

want=int(input("input the number of rank what you want"))

list=[]
list.append(first)
list.append(second)
list.append(third)


if list[0] > list[1]:
    tem=list[0]
    list[0]=list[1]
    list[1]=tem
else:
    if list[1] > list[2]:
        tem = list[1]
        list[1] = list[2]
        list[2] = tem
    else:
        pass



print("The {want} number is {number}".format(number=list[2]),want=want)


class numeric_switch:
    def wordstonumeric(self, arg):
        self.words=getattr(self,self.str(arg),lambda:"default")
        return self.words

    def first(self):
        w_num=1
        return w_num

    def second(self:
        w_num=2
        return w_num

    # def case_default(self):
    #     return "default"



#

for i in len(list):
    if list[i-1]>list[i]:
        tem=list[i-1]
        list[i-1]=list[i]
        list[i]=list[i-1]
    else:
        pass
if list[0] > list[1]:
    tem=list[0]
    list[0]=list[1]
    list[1]=tem
else:
    if list[1] > list[2]:
        tem = list[1]
        list[1] = list[2]
        list[2] = tem
    else: