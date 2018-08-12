
a=[1,2,3,4,5,6]

key=5

return_list=[]

l=0
r=len(a)-1
while l<r:
	addn=a[l]+a[r]
	if a[l]+a[r]==key:
		return_list.append((a[l],a[r]))
		r=r-1
		l=l+1
	else:
		if addn>key:
			r=r-1
		else:
			l=l+1

print return_list
