a = [1,1,1,1,2,2,2,2,3,3,4,5,5,9,9,9]
a = [6,6,3,9,3,5,1]
import itertools

def getMinimumUniqueSum(a):
	from itertools import groupby

	a_new=list(set(a))
	for key, group in groupby(a):
		# print key
		n= len(list(group))

		while n>1:
			new_key=key
			while new_key in a_new:
				new_key=new_key+1
			# print new_key,'-----'
			a_new.append(new_key)
			n=n-1

	# print a_new
	return sum(a_new)

# print getMinimumUniqueSum(a)


def numberOfPairs(a,k):
	# a=
	count=0
	for pair in itertools.combinations(list(set(a)),2):
		if sum(pair)==k:
			# print pair
			count=count+1

	from itertools import groupby
	for key, group in groupby(a):
		print key#,list(group),2*key
		a=list(group)

		print a
		
		# if num>1 and 2*key==k:
		# 	count=count+1



	return count

print numberOfPairs(a,12)