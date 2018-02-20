import urllib2
import json
import datetime

cur_date=datetime.datetime.now()

def compare_lists(l1,l2):
    s=0
    for i in l1:
        if i in l2:
            s+=1
    return s
mynums=[]
m=0
print "dose tous 10 arithmous sou xorizontas tous me space kai patise enter"
s = raw_input()
mynums = map(int, s.split())
for i in range(31):
    cur_date= cur_date - datetime.timedelta(days=1)
    date_str= cur_date.strftime("%d-%m-%Y")
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    data=json.loads(data)
    klhrwseis= data['draws']['draw']
    r=[]
    for k in klhrwseis:
        tmp=k["results"]
        r.append(compare_lists(mynums,tmp))
    print "apotelesmata",date_str
    print "oi perissoteroi arithmoi pou vrikes simera einai",max(r),"kai tous vrikes",r.count(max(r)),"fores"
    if max(r) > 4:
        print "simera einai epitxia"
    else:
        print "simera einai apotxia"
    if r.count(max(r)) > m :
        m=r.count(max(r))
        d=date_str
print "stis",d,"einai i pio tixeri sou mera basi twn arithmwn pou edwses"
