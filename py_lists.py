''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    
    n_of_queries = int(input("Queries count: "))
    n_list=[]
    for i in range(n_of_queries):
        inp= input("Input: ")
        typ = inp.split(' ')
        if typ[0]=='1':
            n_list.append(typ[1])
        elif typ[0]=='2':
            print(n_list)
        else:
            print('Invalid Input')

main()


