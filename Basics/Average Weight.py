"https://workat.tech/problem-solving/practice/average-weight"
# Write your code here
w1,w2, w3, w4, w5, w6, w7, w8, w9, w10=map(float,input().split())

def avg(w1,w2, w3, w4, w5, w6, w7, w8, w9, w10):
	c=w1+w2+w3+w4+w5+w6+w7+w8+w9+w10
	a=c/10
	print("{:.6f}".format(a));
	
avg(w1,w2, w3, w4, w5, w6, w7, w8, w9, w10)
	