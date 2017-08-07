import MySQLdb


class data(object):
#     def __init__(self,conn):
#         self.conn=conn
#         
        
    def connection(self):   
        conn= MySQLdb.connect(
            host='127.0.0.2',
            port = 3306,
            user='root',
            passwd='123456',
            db ='decisiontree',
#             db='test'
            )
        return conn
#         a='hello world'

    
    
    
        
    
# cursor = conn.cursor() 
# cursor.execute('select * from test3')  
#  
# mail_list=[]       
# results = cursor.fetchall()  
# result=list(results)      
# for r in result:      
#     #print 'mail:%s ' % r     
#     mail_list.append(('%s%s' % r))  
# print mail_list  
  
