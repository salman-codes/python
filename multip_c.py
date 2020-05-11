import multiprocessing

def add_two(number):
    print('Addition:' , number + 2)

def subtract_two(number):
    print('Subtraction:' , number - 2)

if __name__ == "__main__":
    number = 7
    
    p1 = multiprocessing.Process(target=add_two, args=(number,))
    p2 = multiprocessing.Process(target=subtract_two, args=(number,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()