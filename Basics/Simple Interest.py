"https://workat.tech/problem-solving/practice/simple-interest"
p,r,t=map(float,input().split())

def intrest(p,r,t):
	
	intrest=p*r*t
	act=intrest/100
	i="{0:.6f}".format(act)
	print(i)
    
	
intrest(p,r,t)	