# import math
import pandas as pd
import numpy as np


# Get  the gamma frequency
def get_gamma_frequency(value_counts, type):
    if type == "g":
        if value_counts[1] > value_counts[0]:
            return 1
        else:
            return 0
    else:
        if value_counts[1] < value_counts[0]:
            return 1
        else:
            return 0


# You need to use the binary numbers in the diagnostic report to generate
# two new binary numbers (called the gamma rate and the epsilon rate).
def get_gamma_rate(df_ge):
    gdig1 = str(get_gamma_frequency(df_ge['Dig1'].value_counts(), "g"))
    gdig2 = str(get_gamma_frequency(df_ge['Dig2'].value_counts(), "g"))
    gdig3 = str(get_gamma_frequency(df_ge['Dig3'].value_counts(), "g"))
    gdig4 = str(get_gamma_frequency(df_ge['Dig4'].value_counts(), "g"))
    gdig5 = str(get_gamma_frequency(df_ge['Dig5'].value_counts(), "g"))
    gamma_rate = gdig1 + gdig2 + gdig3 + gdig4 + gdig5
    return gamma_rate


def get_epsilon_rate(df_ge):
    edig1 = str(get_gamma_frequency(df_ge['Dig1'].value_counts(), "e"))
    edig2 = str(get_gamma_frequency(df_ge['Dig2'].value_counts(), "e"))
    edig3 = str(get_gamma_frequency(df_ge['Dig3'].value_counts(), "e"))
    edig4 = str(get_gamma_frequency(df_ge['Dig4'].value_counts(), "e"))
    edig5 = str(get_gamma_frequency(df_ge['Dig5'].value_counts(), "e"))
    ep_rate = edig1 + edig2 + edig3 + edig4 + edig5
    return ep_rate


# Convert binary to decimal
def binarytodecimal(binary):
    decimal = int(binary, 2)
    return decimal


# The power consumption can then be found by multiplying the gamma rate by the epsilon rate.
# convert the numbers to decimal for the calculation
def get_power_consumption(g_rate, e_rate):
    # bin_g_rate = map(bin, bytearray(g_rate, encoding='utf8'))
    bin_g_rate = g_rate.encode('ascii')
    # bin_e_rate = map(bin, bytearray(e_rate, encoding='utf8'))
    bin_e_rate = e_rate.encode('ascii')
    power_rate = binarytodecimal(bin_g_rate) * binarytodecimal(bin_e_rate)
    return power_rate


class Day3Binary:
    pass


if __name__ == '__main__':
    day3binary = Day3Binary()
    data = np.array([
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 1, 1, 0],
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0]
    ])
    df = pd.DataFrame(data, columns=['Dig1', 'Dig2', 'Dig3', 'Dig4', 'Dig5'])
    # a = int(input("a: "))
    print("gama_rate: ")
    gama_rate = get_gamma_rate(df)
    print(gama_rate)
    print("epsilon_rate: ")
    epsilon_rate = get_epsilon_rate(df)
    print(epsilon_rate)
    print("power_consumption: ")
    power_consumption = get_power_consumption(gama_rate, epsilon_rate)
    print(power_consumption)
