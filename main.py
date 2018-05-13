import json
from pprint import pprint as pp
import matplotlib.pyplot as plt
import numpy as np
from db import get_tickets

from ticket import Ticket
from helpers import date2str

ALPHA = 0.3
BETA = 0.3


if __name__ == "__main__":
    # with open('./tickets.json', 'r') as data_file:
    #     data = json.load(data_file)
    #     tickets = []
    #     for ticket in data.get('tickets'):
    #         tickets.append(Ticket(**ticket))
    #     dates = Ticket.merge_dates(tickets)

    tickets = get_tickets()
    dates = Ticket.merge_dates(tickets)

    array = np.array([0, 0, 0, 0, 0, 0])

    for idx, date in enumerate(sorted(dates)):
        # row = np.array([date2str(date), dates[date], 0, 0, 0, 0])
        row = np.array([idx + 1, dates[date], 0, 0, 0, 0])
        array = np.vstack([array, row])
        # array.append()

    # В качестве y0 берем первое значение ряда, y0 = y1 = 10
    array[0][1] = array[0][2] = array[1][1]
    print('=============================================================')
    print('В качестве y0 берем первое значение ряда, y0 = y1')
    print('array[0][1] = array[0][2] = array[1][1] = ', array[1][1])
    print('=============================================================')
    print('Исходный массив')
    print(array)

    for i in range(1, len(array)):
        print('=============================================================')
        print('array[i][2] = ALPHA * array[i][1] + (1 - ALPHA) * (array[i-1][2] + array[i-1][3])')
        print('array[i][2] = {0:0.3f} * {1:0.3f} + (1 - {0:0.3f}) * ({2:0.3f} + {3:0.3f})'
              .format(ALPHA, array[i][1], array[i-1][2], array[i-1][3]))
        array[i][2] = ALPHA * array[i][1] + (1 - ALPHA) * (array[i-1][2] + array[i-1][3])
        print('array[i][3] = BETA * (array[i][2] - array[i-1][2]) + (1 - BETA)*array[i-1][3]')
        print('array[i][3] = {0:0.3f} * ({1:0.3f} - {2:0.3f}) + (1 - {0:0.3f})*{3:0.3f}'
              .format(BETA, array[i][2], array[i-1][2], array[i-1][3]))
        array[i][3] = BETA * (array[i][2] - array[i - 1][2]) + (1 - BETA) * array[i - 1][3]
        print('array[i][4] = array[i-1][2] + array[i-1][3]')
        print('array[i][4] = {0:0.3f} + {1:0.3f}'.format(array[i-1][2], array[i-1][3]))
        array[i][4] = array[i-1][2] + array[i-1][3]
        print('array[i][5] = abs(array[i][1] - array[i][4]) / array[i][1]')
        print('array[i][5] = abs({0} - {1}) / {0}'.format(array[i][1], array[i][4]))
        array[i][5] = abs(array[i][1] - array[i][4]) / array[i][1]
        print('=============================================================')
    a_l = len(array)
    array = np.vstack([array, np.array([a_l, 0, 0, 0, array[a_l - 1][2] + array[a_l - 1][3], 0])])

    print(array)

    a_l = len(array)

    x1 = [array[i][0] for i in range(1, a_l - 1)]
    y1 = [array[i][1] for i in range(1, a_l - 1)]
    # y2 = [i[2] for i in array if i[0] != 0]
    x2 = [array[i][0] for i in range(1, a_l)]
    y2 = [array[i][4] for i in range(1, a_l)]


    plt.plot(x1, y1, linestyle='--', marker='o', color='b')
    plt.plot(x2, y2, linestyle='--', marker='o', color='orange')
    plt.ylabel('Task execution time')
    plt.xlabel('Number of the week')

    plt.axis([0, 14, 0, 14])
    plt.xticks(range(0, 14))
    plt.yticks(range(0, 14))
    plt.grid(True)
    plt.show()

