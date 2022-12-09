#check 'n' is a prime no. or not

n=int(input("Enter any no. you want to check"))
for i in range(n+1):
	if n%i == 0:
		print("Yes given no.",n,"is prime no.")
