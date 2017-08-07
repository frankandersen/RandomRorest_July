import numpy as np
import matplotlib.pyplot as pl
x=[1,2,3,4,5,6,7,8,9,10]

Improveandomorest=[
0.938453023
,0.944014915
,0.936742557
,0.934945832
,0.937770165
,0.932896745
,0.936583297
,0.951919149
,0.935153332
,0.938006706
]

traditionalRandomForests=[
0.937213228
,0.942431792
,0.935277668
,0.933324561
,0.936053525
,0.931349027
,0.934882988
,0.950175242
,0.933453022
,0.936480804
]


DecisionTree=[
0.931109619
,0.932513428
,0.932208252
,0.928943085
,0.93223877
,0.928027567
,0.93135376
,0.932757568
,0.930316162
,0.930529785
]
                               
SVM=[
0.919512939
,0.920306396
,0.919696045
,0.920296526
,0.921252441
,0.919381008
,0.91975708
,0.920245361
,0.920550537
,0.920153809

]
plot1=pl.plot(x,Improveandomorest,label="$EntropyRf$")
plot2=pl.plot(x,traditionalRandomForests,label="$GeniRf$")
# plot3=pl.plot(x,Initial,label="$Initial$")
plot4=pl.plot(x,DecisionTree,label="$DecisionTree$")
plot5=pl.plot(x,SVM,label="$SVM$")

pl.xlabel('time') 
pl.ylabel('accuracy rate')
# pl.title("PyPlot First Example")
# pl.ylim(0.969,0.972)

pl.legend(loc=3, bbox_to_anchor=[0.8, 0.75])

pl.show()