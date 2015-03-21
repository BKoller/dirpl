import os

def walk(d, i=0):
	for c in os.listdir(d):
		print(i*"  " + c)
		walk(d + '/' + c, i + 1)

def main():
	root = "./test"
	walk(root)

if __name__ == "__main__":
	main()
