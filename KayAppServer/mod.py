import sqlite3;
import os;
print("started")
def cort_to_list(cort):
    list_=[];
    for i in range(len(cort)):
        list_.append(cort[i][0]);
    return list_;

merch=os.listdir("merchants");
for m in merch:
    conn = sqlite3.connect("merchants/"+m+"/orders.sqlite");
    cursor = conn.cursor()
    cursor.execute("INSERT INTO const VALUES((?),(?))",("exNakDriverName","A1",))
    conn.commit();
    conn.close();
print("OK<<<<<<")