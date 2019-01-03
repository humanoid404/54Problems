# execution in jupyter qtconsole is recommended

import numpy as np
import matplotlib.pyplot as plt

data = [[i*j for i in range(13)] for j in range(13)]
columns = [str(i) for i in range(13)]
rows = [str(i) for i in range(13)]

fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
ax.table(cellText=data, rowLabels=rows, colLabels=columns, loc='center')
fig.tight_layout()
plt.show()
