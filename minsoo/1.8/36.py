import math
A = []
a = input('Enter a number ')
s = s_sq = 0
while a != 'done':
    try:
        a = int(a)
        A.append(a)
    except: print('Invalid')
    a = input('Enter a number ')
    M = m = A[0]
print(f'Numbers : {", ".join([str(x) for x in A])}')
class statistics:                                               # 'class'는 다변수함수라고 이해. [f(x,y), g(y,z), h(x,y,z)] 와 같은 모양.
    def __init__(self, set):                                    # def name 꼴에서 'name'이 각각 'coordinate'라고 이해함.
        self.set = set
        self.s = self.s_sq = 0
        self.m = self.M = self.set[0]
        for i in self.set:
            self.s += i
            self.s_sq += i ** 2
            if i < self.m:
                self.m = i
            else: pass
            if self.M < i:
                self.M = i                                      # pass vs continue: 'pass'는 i를 통과시키지만 'continue'는 i를 그 순간 지워버림.
            else: continue                                      # 'for'라는 계곡에서 i(물)가 내려오면, i가 'pass'는 통과하지만 'continue'에게는 막혀서 그 아래로 도달하지 못한다.
    def mean(self):
        result = self.mean = self.s / len(self.set)
        print(f'The average is {result:.0f}.')
        return result
    def max(self):
        result = self.M
        print(f'The maximum is {result}.')
    def min(self):
        result = self.m
        print(f'The minimum is {result}')
    def std(self):
        result = math.sqrt((self.s_sq/len(self.set) - self.mean**2)*len(self.set)/(len(self.set)-1))
        print(f'The standard deviation is {result:.2f}')
b = statistics(A)
b.mean()
b.min()
b.max()
b.std()


# 그냥 문제
# import  math
# A = []
# a = input('Enter a number ')
# s = s_sq = 0
# while a != 'done':
#     try:
#         a = int(a)
#         A.append(a)
#     except: print('Invalid')
#     a = input('Enter a number ')
#     M = m = A[0]
# for i in A:
#     s += i
#     s_sq += i**2
#     if i < m:
#         m = i
#     else: continue
#     if M < i:
#         M = i
#     else: continue
# average = s / len(A)
# std = math.sqrt((s_sq/(len(A)) - average**2)*len(A)/(len(A)-1))
#
# print(f'Numbers : {", ".join([str(x) for x in A])}')
# print(f'The average is {average:.0f}.')
# print(f'The minimum is {m}.')
# print(f'The maximum is {M}.')
# print(f'The standard deviation is {std:.2f}.')