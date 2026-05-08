import numpy as np

def set_param():
    print("input parameter w1: ")
    w1 = float(input())
    print("input parameter w2: ")
    w2 = float(input())
    w = np.array([w1, w2])

    print("input parameter b: ")
    b = float(input())

    return w, b

def and_gate(x1, x2, w, b):
    x = np.array([x1, x2])

    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == "__main__":
    w, b = set_param()
    for x_array in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = and_gate(x_array[0], x_array[1], w, b)
        print(str(x_array) + " -> " + str(y))