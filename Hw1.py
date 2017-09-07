
# Initialize stuff
pattern = "PATTERN"
text = "QWUDQJWNLJWQNRCWEFNPATTERWELJNFLJWENCJWENJKWEWANTTHISPATTERNWEJFNWWEWANTTHISWJEPATTERNFWJEFNW"
endprefix = "5"

LP = len(pattern)
TP = len(text)

# concatenate
pattext = pattern + endprefix + text
LPT = len(pattext)

Zlist = [LP, 0, 0, 0, 0, 0, 0]

k = 2
l = 1
r = 1
i = 2
for k in range(2,LPT):
	If k>r:
		i = 1
		while pattext[k] == pattext[i]:
			i=i+1
		Zlist[k]=i-1
		l=k
		r=k+Zlist[k]-1
	
			
	


