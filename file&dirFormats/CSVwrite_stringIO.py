str='2006-11-13;12.44;44.67'
import csv
def revie(s):
    reader=csv.DictReader(s,delimiter=';')
    for r in reader:
        for k in r.keys():
            print(k,r[k])

from io import StringIO
in_stream=StringIO(str)
revie(in_stream)
in_stream.close()

#write z dictionery CSV plik
data=[[1,'kate'],[2,'paul']]
writer=csv.writer(
    open('out',"w"),
    dialect=csv.excel)
writer.writerows(data)