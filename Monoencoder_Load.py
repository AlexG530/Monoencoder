import numpy as num
import math


# Loads data from .npy files
def beamline_data():
    data_struct = []
    # List files you want to load here

    data_struct.append(num.load('C:/Users/agils/PycharmProjects/monoencoder/csx_data/scans_121472-121499_source_info_mono_mask_temperature_to_shutter_mono_status_rawtimes.npy', allow_pickle=True).tolist())
    data_struct.append(num.load('C:/Users/agils/PycharmProjects/monoencoder/csx_data/scans_121472-121499_source_info_shutter_beamline_status_to_shutter_exitslit_status_rawtimes.npy', allow_pickle=True).tolist())
    data_struct.append(num.load('C:/Users/agils/PycharmProjects/monoencoder/csx_data/scans_121472-121499_source_info_Supply-I_to_I-I_rawtimes.npy', allow_pickle=True).tolist())
    data_struct.append(num.load('C:/Users/agils/PycharmProjects/monoencoder/csx_data/scans_121497-121502_source_info_horz_emit_to_ring_current_rawtimes.npy', allow_pickle=True).tolist())
    data_struct.append(num.load('C:/Users/agils/PycharmProjects/monoencoder/csx_data/scans_121497-121502_source_info_m2DIin_to_grDIout_rawtimes.npy', allow_pickle=True).tolist())
    data_struct.append(num.load('C:/Users/agils/PycharmProjects/monoencoder/csx_data/scans_121497-121502_source_info_P1_CuDI_mix_vlv_to_P1_CuDI_T_rawtimes.npy', allow_pickle=True).tolist())
    data_struct.append(num.load('C:/Users/agils/PycharmProjects/monoencoder/csx_data/scans_121497-121502_source_info_Supply-I_to_I-I_rawtimes.npy', allow_pickle=True).tolist())
    data_struct.append(num.load('C:/Users/agils/PycharmProjects/monoencoder/csx_data/scans_121499-121499_source_info_Supply-I_to_I-I_rawtimes.npy', allow_pickle=True).tolist())

    return data_struct


# Generate test data (delete later)
def test_data():
    line = {}
    hyperbola = {}
    random1 = {}
    random2 = {}
    step = {}
    sigmoid = {}
    sin = {}
    cos = {}
    line_y, hyperbola_y, random1_y, random2_y, step_y, sigmoid_y, sin_y, cos_y, time1, time2 = [], [], [], [], [], [], [], [], [], []
    line['name'], hyperbola['name'], random1['name'], random2['name'], step['name'], sigmoid['name'], sin['name'], cos['name'] = 'Line', 'Hyperbola', 'Random1', 'Random2', 'Step', 'Sigmoid', 'Sine', 'Cosine'
    line['x_avg'], hyperbola['x_avg'], random1['x_avg'], random2['x_avg'], step['x_avg'], sigmoid['x_avg'], sin['x_avg'], cos['x_avg'] = [], [], [], [], [], [], [], []
    line['y_avg'], hyperbola['y_avg'], random1['y_avg'], random2['y_avg'], step['y_avg'], sigmoid['y_avg'], sin['y_avg'], cos['y_avg'] = [], [], [], [], [], [], [], []

    for e in range(100):
        line_y.append(0)
        if e % 5 == 0:
            hyperbola_y.append((2 / (e + 2)) ** 1.5)
            time2.append(e + 1)
        random1_y.append(num.random.randint(0, 1000) / 1000)
        random2_y.append(num.random.randint(0, 1000) / 1000)
        step_y.append(1 / (1 + (2.7182 ** (-4 * e + 200))))
        sigmoid_y.append(1 / (1 + (2.7182 ** (-0.2 * e + 10))))
        sin_y.append(0.5 * math.sin(0.25 * e) + 0.5)
        cos_y.append(0.5 * math.cos(0.25 * e) + 0.5)
        time1.append(e + 1)

    line['x'] = time1
    hyperbola['x'] = time2
    random1['x'] = time1
    random2['x'] = time1
    step['x'] = time1
    sigmoid['x'] = time1
    sin['x'] = time1
    cos['x'] = time1
    line['y'] = line_y
    hyperbola['y'] = hyperbola_y
    random1['y'] = random1_y
    random2['y'] = random2_y
    step['y'] = step_y
    sigmoid['y'] = sigmoid_y
    sin['y'] = sin_y
    cos['y'] = cos_y

    line['x_avg'], hyperbola['x_avg'], random1['x_avg'], random2['x_avg'], step['x_avg'], sigmoid['x_avg'], sin['x_avg'], cos['x_avg'] = num.average(time1), num.average(time2), num.average(time1), num.average(time1), num.average(time1), num.average(time1), num.average(time1), num.average(time1)
    line['y_avg'], hyperbola['y_avg'], random1['y_avg'], random2['y_avg'], step['y_avg'], sigmoid['y_avg'], sin['y_avg'], cos['y_avg'] = num.average(line_y), num.average(hyperbola_y), num.average(random1_y), num.average(random2_y), num.average(step_y), num.average(sigmoid_y), num.average(sin_y), num.average(cos_y)

    return [line, hyperbola, random1, random2, step, sigmoid, sin, cos]


def create_function(a, b, c, kind, interval):
    function0 = []
    function1 = []

    if kind == 'line':
        if interval != 'irregular':
            for s in range(256):
                if s % interval != 0:
                    function0.append(0)
                    function1.append(0)
                else:
                    function0.append(s)
                    function1.append(math.fabs(a))
        else:
            for o in range(256):
                function0.append(0)
                function1.append(0)
            i = num.random.randint(1, 9)
            j = num.random.randint(1, 7)

            for c in range(i):
                c1 = (i*c) + num.random.randint(6, ((256 // i) - 6))
                for d in range(j):
                    d1 = c1 + d
                    function0[d1] = d1
                    function1[d1] = math.fabs(a)

    if kind == 'hyperbola':
        if interval != 'irregular':
            for s in range(256):
                if s % interval != 0:
                    function0.append(0)
                    function1.append(0)
                else:
                    function0.append(s)
                    function1.append(math.fabs(1/((s+1)*4*a)))
        else:
            for o in range(256):
                function0.append(0)
                function1.append(0)
            i = num.random.randint(1, 9)
            j = num.random.randint(1, 7)

            for c in range(i):
                c1 = (i*c) + num.random.randint(6, ((256 // i) - 6))
                for d in range(j):
                    d1 = c1 + d
                    function0[d1] = d1
                    function1[d1] = math.fabs(1/((d1+1)*4*a))

    if kind == 'sinusoid':
        if interval != 'irregular':
            for s in range(256):
                if s % interval != 0:
                    function0.append(0)
                    function1.append(0)
                else:
                    function0.append(s)
                    function1.append(0.5 * math.sin((1/(30 * a)) * s) + 0.5)
        else:
            for o in range(256):
                function0.append(0)
                function1.append(0)
            i = num.random.randint(1, 9)
            j = num.random.randint(1, 7)

            for c in range(i):
                c1 = (i*c) + num.random.randint(6, ((256 // i) - 6))
                for d in range(j):
                    d1 = c1 + d
                    function0[d1] = d1
                    function1[d1] = 0.5 * math.sin((1/(30 * a)) * d1) + 0.5

    if kind == 'sigmoid':
        if interval != 'irregular':
            for s in range(256):
                if s % interval != 0:
                    function0.append(0)
                    function1.append(0)
                else:
                    function0.append(s)
                    function1.append(1 / (1 + (2.7182 ** (b * s + (200 * a)))))
        else:
            for o in range(256):
                function0.append(0)
                function1.append(0)
            i = num.random.randint(1, 9)
            j = num.random.randint(1, 7)

            for c in range(i):
                c1 = (i*c) + num.random.randint(6, ((256 // i) - 6))
                for d in range(j):
                    d1 = c1 + d
                    function0[d1] = d1
                    function1[d1] = 1 / (1 + (2.7182 ** (b * d1 + (100 * a))))

    if kind == 'quadratic':
        if interval != 'irregular':
            for s in range(256):
                if s % interval != 0:
                    function0.append(0)
                    function1.append(0)
                else:
                    function0.append(s)
                    function1.append((1/200) * math.fabs(b) * ((s - 127 + (64 * a)) ** 2))
        else:
            for o in range(256):
                function0.append(0)
                function1.append(0)
            i = num.random.randint(1, 9)
            j = num.random.randint(1, 7)

            for c in range(i):
                c1 = (i*c) + num.random.randint(6, ((256 // i) - 6))
                for d in range(j):
                    d1 = c1 + d
                    function0[d1] = d1
                    function1[d1] = (1/200) * math.fabs(b) * ((d1 - 127 + (64 * a)) ** 2)

    if kind == 'cubic':
        if interval != 'irregular':
            for s in range(256):
                if s % interval != 0:
                    function0.append(0)
                    function1.append(0)
                else:
                    function0.append(s)
                    function1.append(((1/200) * math.fabs(a) * ((s - 127) ** 3)) + (b * ((s - 127) ** 2)) + (c * (s - 127)))
        else:
            for o in range(256):
                function0.append(0)
                function1.append(0)
            i = num.random.randint(1, 9)
            j = num.random.randint(1, 7)

            for c in range(i):
                c1 = (i*c) + num.random.randint(6, ((256 // i) - 6))
                for d in range(j):
                    d1 = c1 + d
                    function0[d1] = d1
                    function1[d1] = ((1/200) * math.fabs(a) * ((d1 - 127) ** 3)) + (b * ((d1 - 127) ** 2)) + (c * (d1 - 127))

    if kind == 'logarithm':
        if interval != 'irregular':
            for s in range(256):
                if s % interval != 0:
                    function0.append(0)
                    function1.append(0)
                else:
                    function0.append(s)
                    function1.append((1/8) * math.fabs(a) * math.log(s+1, 3+b))
        else:
            for o in range(256):
                function0.append(0)
                function1.append(0)
            i = num.random.randint(1, 9)
            j = num.random.randint(1, 7)

            for c in range(i):
                c1 = (i*c) + num.random.randint(6, ((256 // i) - 6))
                for d in range(j):
                    d1 = c1 + d
                    function0[d1] = d1
                    function1[d1] = (1/8) * math.fabs(a) * math.log(d1+1, 3+b)

    if kind == 'random':
        if interval != 'irregular':
            for s in range(256):
                if s % interval != 0:
                    function0.append(0)
                    function1.append(0)
                else:
                    function0.append(s)
                    function1.append(num.random.uniform(0, 1))
        else:
            for o in range(256):
                function0.append(0)
                function1.append(0)
            i = num.random.randint(1, 9)
            j = num.random.randint(1, 7)

            for c in range(i):
                c1 = (i*c) + num.random.randint(6, ((256 // i) - 6))
                for d in range(j):
                    d1 = c1 + d
                    function0[d1] = d1
                    function1[d1] = num.random.uniform(0, 1)

    return [function0, function1]


def training_data(quantity):
    problem_train = []
    answer_train = []
    problem_test = []
    answer_test = []
    transpose = [None, None, None, None]
    function = ['line', 'hyperbola', 'sinusoid', 'sigmoid', 'quadratic', 'cubic', 'logarithmic', 'random']
    interval = [1, 2, 4, 16, 16]
    method = ['Proximity X', 'Proximity Y', 'Interpolation', 'Latest Update']
    print('Generating neural network training data...')

    r1, r2, i, m, a1, b1, c1, a2, b2, c2 = [], [], [], [], [], [], [], [], [], []

    for q in range(quantity):

        r1.append(num.random.randint(0, 8))
        r2.append(num.random.randint(0, 8))
        i.append(num.random.randint(0, 3))
        m.append(num.random.randint(0, 4))
        a1.append(num.random.uniform(-1, 1))
        b1.append(num.random.uniform(-1, 1))
        c1.append(num.random.uniform(-1, 1))
        a2.append(num.random.uniform(-1, 1))
        b2.append(num.random.uniform(-1, 1))
        c2.append(num.random.uniform(-1, 1))
        problem_train.append(0)
        problem_test.append(0)

    for r in range(quantity):

        func_1 = create_function(a1[r], b1[r], c1[r], function[r1[r]], interval[i[r]])
        func_2 = [None, None]

        if method[m[r]] == 'Proximity X':
            func_2 = create_function(a2[r], b2[r], c2[r], function[r2[r]], interval[i[r]])
        if method[m[r]] == 'Proximity Y':
            x0 = []
            shift = num.random.randint(-10, 11)
            for x in func_1[0]:
                if x != 0:
                    x0.append(x + shift)
            func_2[0] = x0
            func_2[1] = func_1[1]
        if method[m[r]] == 'Interpolation':
            func_2 = create_function(a2[r], b2[r], c2[r], function[r2[r]], interval[i[r] + num.random.randint(1, 3)])
        if method[m[r]] == 'Latest Update':
            func_2 = create_function(a2[r], b2[r], c2[r], function[r2[r]], 'irregular')

        transpose[0] = func_1[0]
        transpose[1] = func_1[1]
        transpose[2] = func_2[0]
        transpose[3] = func_2[1]

        if r >= (5 * quantity) // 6:
            problem_train[r] = transpose
            answer_train.append(m[r])
        else:
            problem_test[r] = transpose
            answer_test.append(m[r])
        if r % 100 == 0:
            part = str(r)
            whole = str(quantity)
            print('Progress: ' + part + '/' + whole)

    qty = str(quantity)
    print('Progress: ' + qty + '/' + qty)

    return problem_train, answer_train, problem_test, answer_test
