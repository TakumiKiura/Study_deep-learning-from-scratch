import numpy as np

DEFAULT_W = np.array([0.5, 0.5])
DEFAULT_B = -0.2

def set_param():
    print("input parameter w1: ")
    w1 = float(input())
    print("input parameter w2: ")
    w2 = float(input())
    w = np.array([w1, w2])

    print("input parameter b: ")
    b = float(input())

    return w, b

def or_gate(x1, x2, w = DEFAULT_W, b = DEFAULT_B):
    x = np.array([x1, x2])

    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == "__main__":
    # w, b = set_param()
    for x_array in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = or_gate(x_array[0], x_array[1], DEFAULT_W, DEFAULT_B)  # use default parameters
        print(str(x_array) + " -> " + str(y))