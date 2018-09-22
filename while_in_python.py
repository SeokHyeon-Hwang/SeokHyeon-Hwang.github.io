# sum 1~100
a=1
b=0
while a<=100:
    b += a
    a+=1
print(b)

# sum 1~1000, i%3==0
a=0
b=0
while a<=1000:
	a+=1
	if a%3==0:
		b+=a
	else:
		continue
print(b)

# sum 1~1000, i%3==0
result=0
i=1
while i<=1000:
	if i%3==0:
		result+=i
	i+=1
print(result)

# sum if mark >=50    
a=[20,55,67,82,45,33,90,87,100,25]
result=0
while a:
	mark = a.pop()
	if mark>=50:
		result+=mark
print(result)

# draw stars
i=0
while True:
	i+=1
	if i>5:break
	print('*'*i)
	
i=5
while True:
	print('*'*i)
	i-=1
	if i<0:break
	
i=7
j=0
while i>0:
	if i%2!=0:
		print(' '*j+'*'*i)
	i-=2
	j+=1
