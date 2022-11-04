import requests
import json
import mysql.connector

try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='usdatadb')
except mysql.connector.Error as e:
    print("db connection error")
mycursor=mydb.cursor()
data=requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population").text
data_info=json.loads(data)
for j in data_info['data']:
    #print(str(j['title']))
    idyear=str(j['ID Year'])
    year=str(j['Year'])
    pop=str(j['Population'])
    #sql='INSERT INTO `product`(`title`, `description`, `price`, `discount`, `rating`, `stock`, `brand`, `category`) VALUES ("'+j['title']+'","'+j['description']+'","'+pri+'","'+dis+'","'+rat+'","'+stoc+'","'+j['brand']+'","'+j['category']+'")'
    sql="INSERT INTO `usdata`(`idnation`, `nation`, `idyear`, `year`, `population`, `slugnation`) VALUES ('"+j['ID Nation']+"','"+j['Nation']+"','"+idyear+"','"+year+"','"+pop+"','"+j['Slug Nation']+"')"
    mycursor.execute(sql)
    mydb.commit()
    print("Data inserted successfully",j['ID Nation'])
        