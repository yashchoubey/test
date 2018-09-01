import csv
count=0
cause=''
cisList=[]
causeJson={}
resultJson={}
l1l2=''
key=''
value=''
subject=''
attribute=''
domain=''
department=''
#['L1', 'L2', 'Issue', 'Key', 'Value', 'Department', 'Domain', 'Subject', 'Attribute', 'Questions', 'Solutions', 'Training ', '']
with open('/home/yash/Downloads/L1 & L2 Classification.xlsx - FInal Classification (4).csv', 'rb') as csvfile:
	
	spamreader = csv.reader(csvfile)
	count =0
	for row in spamreader:
		# print row
		# break
		# print row[]
		# if row[1]:
			# print 'yes'
		if row[0] and row[1] and row[2] and row[3] and row[4] and row[5] and row[6] and row[7] and row[8]:
			if l1l2:
				if cause:
					causeJson[cause]=cisList
					cause=row[9]
					cisList=[]
					cisList.append(row[10])
					resultJson[l1l2]=[key,value,department,domain,subject, attribute,causeJson]
					causeJson={}
					# break
			l1l2=row[2]#+":"+ row[1]
			# print l1l2
			key=row[3]
			value=row[4]
			subject=row[7]
			attribute=row[8]
			domain=row[6]
			department=row[5]

		# if not row[0] and row[1]!=None:
		# 	resultJson[l1l2]=[key,value,department,domain,subject, attribute,causeJson]
		# 	causeJson={}
		# 	l1l2=row[2]#l1l2.split(":")[0]+":"+ row[1]
		# 	key=row[3]
		# 	value=row[4]
		# 	subject=row[7]
		# 	attribute=row[8]
		# 	domain=row[6]
		# 	department=row[5]

		if row[9] and row[10]:
			if cause:
				causeJson[cause]=cisList
			cause=row[9]
			cisList=[]
			cisList.append(row[10])
			# print row[10],"=================="

		if  not row[9] and row[10]:
			cisList.append(row[10])
			# print row[10],"=================="

	# for row in spamreader:
	# 	# print row[2]
	# 	# if row[1]:
	# 		# print 'yes'
	# 	if row[0] and row[1]:
	# 		l1l2=str(row[0]+row[1])#row[2]#+":"+ row[1]
	# 		# print l1l2

	# 	if  row[2]:
	# 		# print row[3]
	# 		resultJson[l1l2]=row[2]
	# 		# causeJson={}
	# 		l1l2=row[2]#l1l2.split(":")[0]+":"+ row[1]

import json

print json.dumps(resultJson)