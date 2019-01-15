import re
from tabulate import tabulate
import matplotlib.pyplot as plt

n = 10  # number of words to display
#filename = "46.text"
filename = "46.book"

wordcount = {}
with open(filename, "r") as file:
    for line in file:
        for word in re.finditer(r"(?=(?:^|\W+'*)(\w+(?:'\w+)*)(?:'*\W+|$))", line):
            word = word.group(1).lower()
            if word in wordcount:
                wordcount[word] += 1
            else:
                wordcount[word] = 1

wordcountDescending = sorted([[k, wordcount[k]] for k in wordcount], key=lambda x: x[1], reverse=True)
wcdn = wordcountDescending[:n]
if wcdn[0][1] < 20:
    print(tabulate(map(lambda x: [x[0], "*"*x[1]], wcdn)))

words = list(map(lambda x: x[0], wcdn))
counts = list(map(lambda x: x[1], wcdn))
words.reverse()
counts.reverse()
fig, ax = plt.subplots()
ax.barh(words, counts)
rects = ax.patches
for rect, label in zip(rects, map(str, counts)):
    ax.text(rect.get_x() + rect.get_width(), rect.get_y() + rect.get_height() / 2, label,
            ha='center', va='center')
fig.tight_layout()
plt.show()
