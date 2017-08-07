import csv
c=open("url.csv","w")
writer=csv.writer(c)
writer.writerow(['name','address','city','state'])