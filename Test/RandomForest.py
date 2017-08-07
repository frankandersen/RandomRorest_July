# -*- coding: utf-8 -*- 
import numpy as np  
from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
from mysql import sql
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree  
from sklearn import svm

import csv
from matplotlib.mlab import entropy
#--------------
''' 定义算法类型'''
estimators = {}
  
  
''''' 数据读入 '''  
data   = []  
labels = [] 


conn=sql.data().connection()
cursor = conn.cursor()
 

cursor.execute('select * from 10w_new') 
results = cursor.fetchall() 
# print results 
ifile=list(results)  

for line in ifile:  
    
    data.append(line[1:-1])
    labels.append(line[-1]) 


x = np.array(data)  
y = np.array(labels) 


# print 'x:',x
# print 'y:',y 

''''' 拆分训练数据与测试数据 '''  
feature_train, feature_test, target_train, target_test = train_test_split(x, y, test_size = 0.6)  

#分类型决策树
"""
n_estimators=10：决策树的个数，越多越好，但是性能就会越差，至少100左右（具体数字忘记从哪里来的了）可以达到可接受的性能和误差率。
"""
clf1 = RandomForestClassifier(n_estimators = 10,oob_score=False)
clf = RandomForestClassifier(n_estimators= 60, max_depth=7,criterion= 'entropy',
                              min_samples_split=110,min_samples_leaf=1,oob_score=False,random_state=10)  
rf=RandomForestClassifier(n_estimators= 60, max_depth=7,criterion= 'gini',
                              min_samples_split=110,min_samples_leaf=1,oob_score=False,random_state=10) 
c45=tree.DecisionTreeClassifier(criterion='entropy') 
#支持向量机
SVM=svm.SVC()
#训练模型

s = clf.fit(feature_train , target_train)
s1=rf.fit(feature_train , target_train)
s2=clf1.fit(feature_train , target_train)
trainc45=c45.fit(feature_train , target_train)
trainSVM=SVM.fit(feature_train , target_train)

# print '训练模型：%s' %s

#评估模型准确率
# r = clf.score(feature_test , target_test)
# print '模型准确率:%s'%r
# print('每个属性的重要度:%s'%clf.feature_importances_) 

# ''''' 拆分训练数据与测试数据 '''  
# feature_train, feature_test, target_train, target_test = train_test_split(x, y, test_size = 0.3) 
# ''''' 对样本进行预测'''  
# answer = clf.predict(feature_test)  
# print '测试样本属性：%s'%feature_test
# print'预测结果：%s'% answer
# print'测试样本结果:%s'%target_test
# print'通过对比，验证后的准确度为:%s' %np.mean( answer == target_test)
# a=open("answer.csv","w")
# writer=csv.writer(a)
# writer.writerow(answer)       
# 
# t=open("target_test.csv","w")
# writer=csv.writer(t)
# writer.writerow(target_test)     
#把所有的树都保存到word
# for i in xrange(len(clf.estimators_)):
#     export_graphviz(clf.estimators_[i] , '%d.dot'%i)

print 'entropy:%s'%s.score(feature_test , target_test)
print 'geni:%s' %s1.score(feature_test , target_test)
print 'initial:%s' %s2.score(feature_test , target_test)
print 'DecisionTree:%s' %trainc45.score(feature_test , target_test)
print 'SVM:%s' %trainSVM.score(feature_test , target_test)
