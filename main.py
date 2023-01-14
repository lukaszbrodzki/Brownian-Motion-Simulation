import matplotlib.pyplot as plt
import numpy as np
import xlsxwriter
import sys


def main():
    if len(sys.argv) > 1:
        points = sys.argv[1]

        try:
            points = int(points)
            brown_moves(points)
        except:
            print("Given input is not a number!")
            brown_moves()

    brown_moves()


def brown_moves(points: int = 10000):
    number_sample_points = points
    d = 1
    time_horizon = 1.  # Simulating from time 0 to 1

    times = np.linspace(0., time_horizon, number_sample_points)  # Generating an array with time points
    dt = times[1] - times[0]  # difference between times
    random = np.sqrt(dt) * np.random.normal(size=(number_sample_points - 1, d))
    start_point = np.zeros(shape=(1, d))
    cumulative = np.concatenate((start_point, np.cumsum(random, axis=0)), axis=0)
    plt.plot(times, cumulative)
    plt.show()

    zipped = zip(times, cumulative)

    workbook = xlsxwriter.Workbook('results.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "Time")
    worksheet.write(0, 1, "Point")

    col = 0
    for row, data in enumerate(zipped, start=1):
        worksheet.write_row(row, col, data)

    workbook.close()


if __name__ == '__main__':
    main()
