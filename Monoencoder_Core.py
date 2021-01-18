import matplotlib.pyplot as plot
import math
import numpy as num
from statistics import mean
from tensorflow import keras


# Define correlation analysis methods
def derive(d_func):
    derv = {}
    x = []
    y = []
    if len(d_func['y']) == 1:
        x = d_func['x']
        y = d_func['y']
    else:
        for d in range(len(d_func['y'])):
            if d == 0:
                y.append((2 * ((d_func['y'][d + 1] - d_func['y'][d]) / (d_func['x'][d + 1] - d_func['x'][d]))) ** 2)
                x.append(d_func['x'][d])
            elif d == (len(d_func['y']) - 1):
                y.append((2 * ((d_func['y'][d - 1] - d_func['y'][d]) / (d_func['x'][d - 1] - d_func['x'][d]))) ** 2)
                x.append(d_func['x'][d])
            else:
                y.append((2 * ((d_func['y'][d+1] - d_func['y'][d-1])/(d_func['x'][d+1] - d_func['x'][d-1]))) ** 2)
                x.append(d_func['x'][d])
    derv['name'] = "d_" + d_func['name']
    derv['x'] = x
    derv['y'] = y
    return derv


# Normalize the organized data
def normalize(data):
    y_high = num.max(data['y'])
    y_low = num.min(data['y'])
    scope = y_high - y_low
    for sub in range(len(data['y'])):
        if scope != 0:
            data['y'][sub] = (data['y'][sub] - y_low) / scope
        else:
            data['y'][sub] = 1

    return data


def resize(func_j, func_k):
    j_low = num.min(func_j['x'])
    j_high = num.max(func_j['x'])
    k_low = num.min(func_k['x'])
    k_high = num.max(func_k['x'])

    if j_low <= k_low:
        low = j_low
    else:
        low = k_low
    if j_high >= k_high:
        high = j_high
    else:
        high = k_high
    scale = high - low

    input = []
    for i in range(4):
        line = []
        for n in range(256):
            line.append(0)
        input.append(line)
        line.clear()

    for j in range(len(func_j['x'])):
        inx = (256 * (func_j['x'][j] - low)) // scale
        input[0][inx] = func_j['x'][j] - low
        input[1][inx] = func_j['y'][j] - low
    for k in range(len(func_k['x'])):
        inx = (256 * (func_k['x'][k] - low)) // scale
        input[2][inx] = func_k['x'][k] - low
        input[3][inx] = func_k['y'][k] - low

    return input


def load_CNN():
    try:
        model = keras.models.load_model('Monoencoder_CNN')
        return model
    except:
        print('ERROR: The neural network model "Monoencoder_CNN" could not be retrieved. To correct this error, '
              'please do the following:')
        print('\n1: Open this repository in an IDE that supports Python 3.7.'
              '\n2: Locate the .py file "Monoencoder_CNN and open it.'
              '\n3: Run Monoencoder_CNN.')


def match(f_base, f_subject, method):
    pairs = []
    if method == 'Proximity X':
        for s in range(len(f_subject['x'])):
            links = []
            for b in range(len(f_base['x'])):
                t = (b, math.fabs(f_base['x'][b] - f_subject['x'][s]))
                links.append(t)
            val0 = 0
            val1 = 100
            for l in links:
                if l[1] < val1:
                    val0 = l[0]
                    val1 = l[1]
            pairs.append((val0, s))
        return pairs

    elif method == 'Interpolation':
        for s in range(len(f_subject['x'])):
            for b in range(len(f_base['x'])):
                if f_subject['x'][s] <= f_base['x'][0]:
                    pairs.append((0, s))
                    break
                elif f_base['x'][b-1] < f_subject['x'][s] <= f_base['x'][b]:
                    x = f_subject['x'][s]
                    x1 = f_base['x'][b - 1]
                    x2 = f_base['x'][b]

                    xx = (x - x1) / (x2 - x1)

                    pairs.append((b-1+xx, s))
                    break
                elif f_subject['x'][s] >= f_base['x'][-1]:
                    pairs.append(((len(f_base['x']) - 1), s))
                    break
        return pairs

    elif method == 'Proximity Y':
        for s in range(len(f_subject['x'])):
            links = []
            for b in range(len(f_base['x'])):
                t = (b, math.fabs(f_base['y'][b] - f_subject['y'][s]))
                links.append(t)
            val0 = 0
            val1 = 10
            for l in links:
                if math.fabs(f_base['x'][l[0]] - f_subject['x'][s]) < 10:
                    if l[1] < val1:
                        val0 = l[0]
                        val1 = l[1]
            pairs.append((val0, s))
        return pairs

    elif method == 'Latest Update':
        for s in range(len(f_subject['x'])):
            for b in range(len(f_base['x'])):
                if f_subject['x'][s] <= f_base['x'][0]:
                    pairs.append((0, s))
                    break
                elif f_base['x'][b - 1] < f_subject['x'][s] <= f_base['x'][b]:
                    pairs.append((b-1, s))
                    break
                elif f_subject['x'][s] > f_base['x'][-1]:
                    pairs.append(((len(f_base['x']) - 1), s))
                    break
        return pairs

    else:
        return None


def p1p2(point_1x, point_1y, point_2x, point_2y, offset=0):
    dis = ((((point_2x - point_1x) - offset) ** 2) + ((point_2y - point_1y) ** 2)) ** 0.5
    if dis > 1:
        dis = 1
    return 1 - dis


def d1d2(point_d1, point_d2):
    point_d1 = math.fabs(point_d1)
    point_d2 = math.fabs(point_d2)
    if point_d1 <= 1/(2 ** 16):
        point_d1 = 1/(2 ** 16)
    if point_d2 <= 1/(2 ** 16):
        point_d2 = 1/(2 ** 16)

    skew = math.atan(math.fabs(point_d2 - point_d1) / point_d1) / (num.pi / 2)
    return 1 - skew


# Output a graph of the two functions being compared.
# func_a is the 'baseline' function that func_b will be compared to
def graph(data, f1, f2, count, func_c=None):
    rows = int((count ** 0.5) // 1) + 1
    n = 0
    fig, sub = plot.subplots(rows, rows)
    for c in range(rows):
        for d in range(rows):
            if n < count:
                func_a = data[f1[n]]
                func_b = data[f2[n]]
                sub[d, c].scatter(func_a['x'], func_a['y'], c='gray', alpha=0.5)
                for t in range(len(func_b['x']) - 1):
                    if func_c is None:
                        rho = p1p2(func_a['x'][t], func_a['y'][t], func_b['x'][t], func_b['y'][t])
                    else:
                        rho = func_c[n][t]

                    if rho == 0:
                        color = '#ff0000'
                    elif rho < 1/16:
                        color = '#f01000'
                    elif rho < 2/16:
                        color = '#e02000'
                    elif rho < 3/16:
                        color = '#d03000'
                    elif rho < 4/16:
                        color = '#c04000'
                    elif rho < 5/16:
                        color = '#b05000'
                    elif rho < 6/16:
                        color = '#a06000'
                    elif rho < 7/16:
                        color = '#907000'
                    elif rho < 8/16:
                        color = '#808000'
                    elif rho < 9/16:
                        color = '#709000'
                    elif rho < 10/16:
                        color = '#60a000'
                    elif rho < 11/16:
                        color = '#50b000'
                    elif rho < 12/16:
                        color = '#40c000'
                    elif rho < 13/16:
                        color = '#30d000'
                    elif rho < 14/16:
                        color = '#20e000'
                    elif rho < 15/16:
                        color = '#10f000'
                    else:
                        color = '#00ff00'

                    sub[d, c].scatter(func_b['x'][t], func_b['y'][t], c=color, alpha=0.5)

                sub[d, c].set_title(func_a['name'] + ' vs ' + func_b['name'])

                n += 1


# Compare 2 functions to each other. For more than 2 functions, iterate over a pair
# of for loops to compare each function to each other function
def compare(func_1, func_2, method=None):
    d_func_1 = derive(func_1)
    d_func_2 = derive(func_2)
    average = []
    d_average = []
    c_total = []

    pairs = match(func_1, func_2, method)

    if pairs is None:
        for j in range(len(func_1['x'])):
            average.append(p1p2(func_1['x'][j], func_1['y'][j], func_2['x'][j], func_2['y'][j]))
        for k in range(len(d_func_1['x'])):
            d_average.append(d1d2(d_func_1['y'][k], d_func_2['y'][k]))
        for l in range(len(d_average)):
            c = (((average[l] ** 2) + (3 * (d_average[l] ** 2))) ** 0.5) / 2
            c_total.append(c)
    else:
        if method == 'Proximity X':
            for j in pairs:
                average.append(p1p2(func_1['x'][j[0]], func_1['y'][j[0]], (func_2['x'][j[1]]), func_2['y'][j[1]]))
                d_average.append(d1d2(d_func_1['y'][j[0]], d_func_2['y'][j[1]]))
        elif method == 'Proximity Y':
            shift = []
            for p in pairs:
                shift.append(func_1['x'][p[0]] - func_2['x'][p[1]])
            try:
                offset = mean(shift)
            except:
                offset = num.average(shift)
            for j in pairs:
                average.append(p1p2(func_1['x'][j[0]], func_1['y'][j[0]], (func_2['x'][j[1]]), func_2['y'][j[1]], offset))
                d_average.append(d1d2(d_func_1['y'][j[0]], d_func_2['y'][j[1]]))
        elif method == 'Interpolation':
            for j in pairs:
                inx = j[1] // 1
                yy = j[1] % 1
                if yy != 0:
                    y1 = func_2['y'][inx]
                    y2 = func_2['y'][inx+1]
                    y = yy * (y2 - y1) + y1
                else:
                    y = func_2['y'][inx]
                average.append(p1p2(func_1['x'][int(j[0])], func_1['y'][int(j[0])], func_1['x'][int(j[0])], y))
                d_average.append(d1d2(d_func_1['y'][int(j[0])], d_func_2['y'][int(inx)]))
        elif method == 'Latest Update':
            for j in pairs:
                average.append(p1p2(func_1['x'][j[0]], func_1['y'][j[0]], func_1['x'][j[0]], func_2['y'][j[1]]))
                d_average.append(d1d2(d_func_1['y'][j[0]], d_func_2['y'][j[1]]))
        for l in range(len(pairs)):
            c = (((average[l] ** 2) + (3 * (d_average[l] ** 2))) ** 0.5) / 2
            c_total.append(c)

    return num.average(c_total), c_total
