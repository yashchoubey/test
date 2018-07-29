with open("tourist_output.txt",'w') as ofile:

	with open("tourist.txt",'r') as ifile:
		totalcases = int(ifile.readline().replace('\n',''))
		for i in range(1,totalcases+1):
			N,K,V= map(int,(ifile.readline().replace('\n','').split(' ')))
			refdict={}
			for j in range(0,N):
				refdict[j]=ifile.readline().replace('\n','')
			# print refdict

			result=''
			count=0
			start= (K*(V-1))%N
			# print start
			while count < K:
				if N-start<K:
					for k in range(0,K-N+start):
						if count < K:
							result=result+" "+refdict[k]
							count=count+1

				for k in range(start,N):

					if count < K:
						result=result+" "+refdict[k]
						count=count+1


			print "Case #%i:%s"%(i,result)
			ofile.write("Case #%i:%s\n"%(i,result))