import pickle

x=[]
correct_list=[]
incorrect_list=[]


with open('/home/yash/bitbucket/haikujam-nlp/test and data/data/fake_words.txt', "rb") as fp:   #Pickling
    x=pickle.load( fp)

with open('/home/yash/bitbucket/haikujam-nlp/test and data/data/correct_words.txt', "rb") as fp:   #Pickling
    correct_list=pickle.load( fp)


with open('/home/yash/bitbucket/haikujam-nlp/test and data/data/incorrect_words.txt', "rb") as fp:   #Pickling
    incorrect_list=pickle.load( fp)

# print correct_list,incorrect_list

from spell_check_pyenchant import spell_check
for word in x[:20]:
    # print 'here'
    if word not in correct_list and  word not in incorrect_list :
        ans=int( spell_check(word)['spellError'])
        if ans > 0:
            # print k
            print word
            choice = input("choice : ")
            # print choice,'77777777777'
            if choice==0:
                correct_list.append(word)

            else:
                incorrect_list.append(word)

    x.remove(word)





correct_list=list(set(correct_list))
incorrect_list=list(set(incorrect_list))


with open('/home/yash/bitbucket/haikujam-nlp/test and data/data/correct_words.txt', "wb") as fp:   #Pickling
    pickle.dump(correct_list, fp)

with open('/home/yash/bitbucket/haikujam-nlp/test and data/data/incorrect_words.txt', "wb") as fp:   #Pickling
    pickle.dump(incorrect_list, fp)

with open('/home/yash/bitbucket/haikujam-nlp/test and data/data/fake_words.txt', "wb") as fp:   #Pickling
    pickle.dump(x, fp)

