"https://workat.tech/problem-solving/practice/candies"
# Write your code here
c,ca=map(int,input().split())

def candies(c,ca):
	if c%ca==0:
		print("YES")
	else:
		print("NO")
		
candies(c,ca)