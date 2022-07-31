# from nltk.tokenize import sent_tokenize, word_tokenize
# import warnings
# import json
# warnings.filterwarnings(action = 'ignore')

# import gensim
# from gensim.models import Word2Vec

  

# f = open('templates.json')
# sample = open("template_APP1.txt","w")
# data = json.load(f)
# r = len(data)
# count = 0

# for key,value in data.items():
#     sample.write(value)
#     count+=1
#     if(count==r):
#         break
#     sample.write("\n")
  
# f.close()
# sample.close()

# sample = open("template_APP1.txt","r")
# s = sample.read()

# f = s.replace("\n", " ")

# data = []

# for i in sent_tokenize(f):
# 	temp = []
	
	
# 	for j in word_tokenize(i):
# 		temp.append(j.lower())

# 	data.append(temp)

# model1 = gensim.models.Word2Vec(data, min_count = 2,
# 							vector_size = 100, window = 5)

# model1.build_vocab(data,progress_per=1000)

# print(data)


data = [1,2,3,4,5,6,7,8,9,10,11,12,13]
for i in enumerate(data):
    print(i)