''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import numpy as np
def main():
    a = input()
    b = a.split(' ')
    c = np.reshape(b,(3,3))
    print(c)
main()

