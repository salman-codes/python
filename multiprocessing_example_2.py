import multiprocessing as p
import time as t

def f1(num):
	for n in num:
		t.sleep(3)
		print(n * n)

def f2(num):
	for n in num:
		t.sleep(5)
		print(n * n * n)

if __name__ == '__main__':
	nums = [3, 7, 4]
	process1 = p.Process(target=f2, args=(nums,))
	process2 = p.Process(target=f1, args=(nums,))

	process1.start()
	process2.start()

	process1.join()
	process2.join()

	print("Finished!")