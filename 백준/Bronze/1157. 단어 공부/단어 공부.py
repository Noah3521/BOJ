N = input().upper().rstrip()
setN = list(set(N))
 
mx = 0
result = ''
for i in setN:
	n = N.count(i)
	if mx < n:
		mx = n
		result = i
	elif mx == n:
		result = '?'
print(result)