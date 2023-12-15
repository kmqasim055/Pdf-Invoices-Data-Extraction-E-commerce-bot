#!/usr/bin/env python
# coding: utf-8

# In[143]:


import os
import fitz
import time
import pandas as pd


# In[120]:


# doc = fitz.open("5366650.pdf")
# page_count = doc.page_count
# docs = doc[0].get_text().split('\n')
# print(docs)


# In[121]:


# doc = fitz.open("5368047.pdf")
# page_count = doc.page_count
# docs = doc[0].get_text().split('\n')
# print(docs)


# In[146]:


l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
l7 = []
l8 = []
l9 = []
l10 = []
check = []
s1 = ""
s2 = ""
s3 = ""
extra = False

ch1 = True
flag = True
flag2 = True
count = 0
lis = 0

cwd = os.getcwd()
dir_path = os.path.join(cwd, 'pdfs')
for filename in os.listdir(dir_path):
    if filename.endswith('.pdf'):
        doc = fitz.open(os.path.join(dir_path, filename))
        page_count = doc.page_count
        print("Current PDF Processing : ", os.path.basename(filename))
        time.sleep(0.25)
        
        for j in range(page_count):
            docs = doc[j].get_text().split('\n')

            extra = False
            ch1 = True
            flag = True
            flag2 = True
            count = 0
            lis = 0

            for i in docs:
                if(extra == True):
                    extra = False
                    count+=1
                    continue
                if(flag == False):
                    flag = True
                    s1 = i
                if(i.find('Delivery-address') != -1):
                    flag = False
                if(i.find('Date of order') != -1):
                    #print(i.split(': ')[1])
                    s2 = i.split(': ')[1]
                    s2 = s2.split('.')[1] + '/' + s2.split('.')[0] + '/' + s2.split('.')[2]
                if(i.find('Reference:') != -1):
                    s8 = i.split(': ')[1]
                if(i.find('Forwarder') != -1):
                    #print(docs[count - 1])
                    co = 0
                    for rec in docs:
                        if(docs[count - 1] == rec):
                            co+=1
                    if(co == 2):
                        s3 = 'No Number'
                    elif(co == 1):
                        s3 = docs[count - 1]

                if(i.find('/') != -1 and i[len(i) - 1] >= '0' and i[len(i) - 1] <= '9'):
                    #print(i.split('/')[0])
                    s4 = i.split('/')[0]
                    #print(i.split('/')[1])
                    s5 = i.split('/')[1]
                    #print(docs[count + 1].split()[0])
                    s6 = ''.join(docs[count + 1].split()[:-1])
                    #print(docs[count + 4])
                    s7 = docs[count + 4]
                    
                    var = 1
                    for ran in range(len(check) -1 , -1, -1):
                        l5.insert(check[ran], docs[count - 1 - var])
                        #print(l5)
                        var+=1
                    check = []
                try:
#                     if(i.find("Meyer-Hosen-AG") != -1):
#                         if(docs[count - 1] == 'NOS' or docs[count - 1] == 'DEPOT'):
#                             var = 1
#                             for ran in range(len(check) -1 , -1, -1):
#                                 l5.insert(check[ran], docs[count - 2 - var])
#                                 var+=1
#                         else:
                    
                    if(i.find("Meyer-Hosen-AG") != -1 or i.find("Terms of payment: 180 days net 0.0%") != -1):
                        var = 1
                        for ran in range(len(check) -1 , -1, -1):
                            l5.insert(check[ran], docs[count - var])
                            #print(l5)
                            var+=1
                        check = []
                    if(int(docs[count][0:2]) >= 30 and int(docs[count][0:2])<= 46 and len(i) == 3 and (docs[count][-1] == 'L' or docs[count][-1] == 'R' or docs[count][-1] == 'S') and docs[count+2 ] != 'NOS' and docs[count+2 ] != 'DEPOT'  and docs[count - 1 ] != 'Composition' and docs[count - 1 ] != 'Page' and docs[count + 2 + len(check)].find("Meyer-Hosen-AG") == -1 and docs[count + 2 + len(check)].find("Terms of payment: 180 days net 0.0%") == -1):
                        ch1 = False
                        if(docs[count+3].find('/') == -1):
                            try:
                                if(int(docs[count+1]) < int(docs[count][0:2])):
                                    if(docs[count][len(docs[count]) -1] == 'L'):
                                        temp = docs[count].split('L')[0]
                                        temp+='34'
                                        #print(temp)
                                    elif(docs[count][len(docs[count]) -1] == 'R'):
                                        temp = docs[count].split('R')[0]
                                        temp+='32'
                                    elif(docs[count][len(docs[count]) -1] == 'S'):
                                        temp = docs[count].split('S')[0]
                                        temp+='30'
                                    if(docs[count+1] == '0'):
                                        #print(len(l5), l5)
                                        check.append(len(l5))
                                    else:     
                                        l5.append(docs[count+1])
                                    l4.append(temp)
                                    l1.append(s6+s4+s5+l4[len(l4) -1])
                                    l6.append(s7)
                                    l7.append(s1)
                                    l8.append(s2)
                                    l9.append(s3)
                                    l10.append(s8)
                                    extra = True
                            except:
                                pass
                        

                    elif(int(i) >= 23 and int(i)<= 118 and docs[count+2 ] != 'NOS' and docs[count+2 ] != 'DEPOT'  and docs[count - 1 ] != 'Composition' and docs[count - 1] != 'Page' and docs[count + 2 + len(check)].find("Meyer-Hosen-AG") == -1 and docs[count + 2 + len(check)].find("Terms of payment: 180 days net 0.0%") == -1):
                        #print("hduhduw", i)
                        ch1 = False
                        if(docs[count+3].find('/') == -1):
                            try:
                                if(int(docs[count+1]) < int(docs[count])):
                                    #print("####################", docs[count+1], "##", int(i))
                                    if(docs[count+1] == '0'):
                                        #print(len(l5), l5)
                                        check.append(len(l5))
                                    else:     
                                        l5.append(docs[count+1])
                                    l4.append(docs[count])
                                    l1.append(s6+s4+s5+l4[len(l4) -1])
                                    l6.append(s7)
                                    l7.append(s1)
                                    l8.append(s2)
                                    l9.append(s3)
                                    l10.append(s8)
                                    extra = True
                            except:
                                pass
                except:
                    pass
                count+=1
        doc.close()
        
        l1 = [x.upper() for x in l1]
        l5 = [x.upper() for x in l5]
        l6 = [x.upper() for x in l6]
        l7 = [x.upper() for x in l7]
        l8 = [x.upper() for x in l8]
        l9 = [x.upper() for x in l9]
        l10 = [x.upper() for x in l10]
        
        Stocks=pd.DataFrame(zip(l1, l5, l6, l7, l8, l9, l10),
               columns =['Sku', 'Quantity', 'Price', 'Customer', 'Date', 'Order', 'Reference'])
        Stocks.to_csv(l10[0] + '.csv', index=False, encoding='utf-8-sig')
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        l5 = []
        l6 = []
        l7 = []
        l8 = []
        l9 = []
        l10 = []
        check = []


# In[144]:


# import pandas as pd
# Stocks=pd.DataFrame(zip(l1, l5, l6, l7, l8, l9, l10),
#                columns =['Sku', 'Quantity', 'Price', 'Customer', 'Date', 'Order', 'Reference'])
# Stocks.to_csv("Stocks.csv", index=False, encoding='utf-8-sig')


# In[145]:


# df = pd.read_csv('Stocks.csv')
# df


# In[ ]:




