#!/usr/bin/env python
# coding: utf-8

# # 功課ㄧ - Extract Terms for Document
# * Tokenization
# * Lowercasing everything.
# * Stemming using Porter’s algorithm.
# * Stopword removal.
# * Save the result as a txt file. 
# 


# In[22]:


with open('./hw1.txt') as f:
    lines = f.readlines()


# In[23]:


#print(lines)


# ## To lower case

# In[61]:


doc_list = [i.lower().rstrip(' ').rstrip('\n').rstrip('.')for i in lines]


# In[62]:

#print(doc_list)


# ## Stemming
# * [gensim porter](https://radimrehurek.com/gensim/parsing/porter.html)

# In[63]:


from nltk.stem import PorterStemmer
p = PorterStemmer()
stemmed_doc =[]

for token in doc_list:
    stemmed_doc.append(p.stem(token))


# In[64]:


# print(stemmed_doc)


# ## Tokenization

# In[68]:


tokens = [i.split(' ') for i in stemmed_doc]


# In[69]:


# print(tokens)


# ## Remove stopwords

# In[74]:


final_tokens =[]

with open ('./stopwords.txt') as f:
    stop_words = f.readlines()
stop_words = [words.strip('\n') for words in stop_words]

for l in tokens:
    for word in l:
        word = word.rstrip('.').rstrip('\'').rstrip(',')
        if word not in final_tokens and word not in stop_words and len(word)>0:
            final_tokens.append(word)


# In[75]:


# print(final_tokens)


# In[76]:


# save as txt file
with open('result.txt', 'w') as f:
    for line in final_tokens:
        f.write(f"{line}\n")


# In[ ]:




