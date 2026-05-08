import numpy as np

from and_gate import and_gate
from nand_gate import nand_gate
from or_gate import or_gate

def xor_gate(x1, x2):
    y_nand = nand_gate(x1, x2)
    y_or = or_gate(x1, x2)
    y = and_gate(y_nand, y_or)
    return y

if __name__ == "__main__":
    # w, b = set_param()
    for x_array in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = xor_gate(x_array[0], x_array[1])
        print(str(x_array) + " -> " + str(y))