# coding='utf-8'
import os
import math
 
def get_tf(text):
	"""
	计算tf值
	text:该词所在文档
	return:dict word_tf(该文本出现的词的tf值)
	"""
	num_words = len(text)
	word_freq = {} #词频dict
	word_tf = {} #词的tf值dict
	for i in range(num_words):
		word_count = 1
		for j in range(num_words):
			if i!=j and text[i]!=" ":
				if text[i] == text[j]:
					word_count += 1
					text[j] = " "	
		if text[i] != " ":
			#word_freq[text[i]] = word_count
			word_tf[text[i]] = float(word_count / num_words)
 
	return word_tf
 
def get_idf(word,corpus_list):
	"""
	计算idf值
	word：要计算的词
	corpus_list:包含所有语料的list，一个文件为其中一个元素
	return:该词的idf值
	"""
	num_corpus = len(corpus_list)
	count = 0
	for cur_corpus in corpus_list:
		if word in set(cur_corpus):
 
			count += 1
	idf = math.log(float(num_corpus / (count + 1)))
 
	return idf
 
def get_tfidf(cur_corpus,corpus_list):
	"""
	分文本计算tfidf值
	cur_corpus:当前文本
	corpus_list：所有文本的list
	"""
	cur_word_tfidf = {}
	word_tf = get_tf(cur_corpus)
	for word in word_tf:
		tf = word_tf[word]
		idf = get_idf(word,corpus_list)
		cur_word_tfidf[word] = tf*idf
	print(cur_word_tfidf)
 
	return cur_word_tfidf
 
def get_corpus(path):
	"""
	获得路径下的所有文本的list，每个文本按空格分为list，形式为[[],[],[],·····]
	path：语料路径
	return：corpus_list语料  files_list语料文件名称
	"""
	corpus_list = []
	files_list = get_files(path)
	for cur_filename in files_list:
		f = open(str(path + "/" + cur_filename))
		cur_file = f.read().replace("\n"," ")
		cur_file = cur_file.split(" ")
		corpus_list.append(cur_file)
		f.close()
 
	return corpus_list,files_list
 
def get_files(path):
	"""
	获取文件目录，返回文件名list
	"""
	files_list = os.listdir(path)
	return files_list
 
def get_tfidf_file(path):
	"""
	分文本计算tfidf，并将结果分别写到相应文件中
	path：语料路径
	"""
	corpus_list,files_list = get_corpus(path)
	num_corpus = len(corpus_list)
	for i in range(num_corpus):
		word_tfidf = get_tfidf(corpus_list[i],corpus_list)
		cur_filename = files_list[i]
		cur_file = open(path+"/"+cur_filename+"_tfidf.txt","w")
		for cur_word in word_tfidf:
			cur_file.write(cur_word + ":" + str(word_tfidf[cur_word])+"\n")
		cur_file.close()
	return True
	
# get_tfidf_file("")

