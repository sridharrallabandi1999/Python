"https://workat.tech/problem-solving/practice/temperature-conversion"
# Write your code here
	
try:
	t  = int(input())
	while(t):
		n = float(input())
		f = (9*n/5)+32
		print("%.2f"%f)
		t-=1
except:EOFError