class Person:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.fullname = first + ', ' + last

    def __repr__(self):
        return repr(self.first + ' ' + self.last)


p1 = Person('Ling', 'Mai')
p2 = Person('Johnson', 'Jim')
p3 = Person('Zarnecki', 'Sabrina')

total_person = [p1, p2, p3]

data = (sorted(total_person, key=lambda x: x.fullname))

# print(f"Total of {len(total_person)} names",'-'*10,data.split(','),sep='\n')

print(f"Total of {len(total_person)} names", '-' * 10, sep='\n')


for i in data:
    print(i)

