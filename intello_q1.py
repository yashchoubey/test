a=[0,1,2,0,1,0,1,2,1,1,2,1,2]

count0=0
count2=len(a)-1


i=0
while count2>=count0 and count2>=i:
	
	if a[i]==0:
		a[i]=1
		a[count0]=0
		count0=count0+1

	elif a[i]==2:
		if a[count2]==2:
			while a[count2]==2:
				count2=count2-1

		a[i]=1
		a[count2]=2
		count2=count2-1

	i=i+1

print a