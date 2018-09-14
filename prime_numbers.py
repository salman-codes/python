''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

import math
def main():
    n1 = int(input())
    n2=int(input())
    
    if n1 < n2:
        for i in range(n1, n2):
            flag = True
            for j in range(2, i-1):
                if i%j == 0:
                    flag = False
            if flag==True:
                print(i)

main()
