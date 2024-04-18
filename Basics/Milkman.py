# Write your code here
"https://workat.tech/problem-solving/practice/milkman"

r,h=map(float,input().split())

def milk(r,h):
	V=((3.14*(r**2)*h)/1000)
	price=(40*V)
	print("{:.2f}".format(price));
	
	
milk(r,h)