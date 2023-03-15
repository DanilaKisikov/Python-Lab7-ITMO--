import matplotlib.pyplot as plt
import numpy as np
import csv


## 1-4 и 16

def graph(x, y, color):
    plt.plot(x, y, color)


if __name__ == "__main__":
    table = np.genfromtxt("data1.csv", delimiter=";")

    with open('data1.csv', 'r') as file:
        row = list(csv.reader(file, delimiter=';'))[0]

        firstName  = row[0]
        fourthName = row[3]
        sixteenthName = row[15]

    firstCol = table[1:, 0]
    fourthCol = table[1:, 3]
    sixteenthCol = table[1:, 15]

    correlation = np.subtract(sixteenthCol, fourthCol)

    graph(firstCol, fourthCol, "b")
    graph(firstCol, sixteenthCol, "r")
    graph(firstCol, correlation, "g")

    plt.xlabel(firstName)
    plt.ylabel(fourthName + "\n and \n" + sixteenthName)

    plt.show()
