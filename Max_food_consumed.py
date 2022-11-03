import csv
ea=0
with open('log_res.csv','r') as f:
    f_read=csv.reader(f)
    fields=next(f_read)
    rows=[i for i in f_read]
for i in rows:
    if i[0]==i[1]:
        ea+=1
if ea>1:  
    print('both eaten id and foodmenu id are occured more than once')    
else:            
    foodmenu_ids=[i[1] for i in rows]
    d={i:0 for i in sorted(foodmenu_ids)}
    for i in sorted(foodmenu_ids):
        d[i]+=1
    sorted_dict={k:v for k,v in reversed(sorted(d.items(), key=lambda item: item[1]))}
    max3consumers={k:sorted_dict[k] for k in list(sorted_dict)[:3]}
    print(max3consumers)