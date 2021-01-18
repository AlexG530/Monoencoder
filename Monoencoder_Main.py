import numpy as num
import matplotlib.pyplot as plot
from Monoencoder_Load import test_data, beamline_data
import Monoencoder_Core
from Monoencoder_CNN import method_select

# Load and organize data
test = True
if test:
    raw_data = test_data()
else:
    raw_data = beamline_data()

data = []
# Function format:
# name = the name of the pv
# x = times in seconds
# y = pv values

if not test:
    for r in raw_data:
        sets = list(r)
        for s in sets:
            dat = {'name': s, 'x': r[s]['seconds'], 'y': r[s]['pvdata'], 'x_avg': num.average(r[s]['seconds']), 'y_avg': num.average(r[s]['pvdata'])}
            data.append(dat)

method = ['Proximity X', 'Proximity Y', 'Interpolation', 'Latest Update']
# model = Monoencoder_Core.load_CNN()
t = 1
charts = 0
sets = []
f1 = []
f2 = []
for u in range(len(data) - 1):
    for v in range(t, len(data)):
        # x = Monoencoder_Core.resize(data[u], data[v])
        # y = method_select(model, x)
        y = num.random.randint(0, 4)
        corr, pairs = Monoencoder_Core.compare(data[u], data[v], method[y])
        if corr >= 0.6:
            print('There is a ' + f'{corr*100: .2f}' + '% chance that ProcessVariables ' + data[u]['name'] + ' and ' + data[v]['name'] + ' are correlated.')
            charts += 1
            sets.append(pairs)
            f1.append(u)
            f2.append(v)
    t += 1

Monoencoder_Core.graph(data, f1, f2, charts, sets)
plot.show()
