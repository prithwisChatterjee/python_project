import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="10.40.2.16",
  user ="prithwis",
  passwd ="Prithwis#434",
  database = "dev_syscontrol"
)
cursorObject = dataBase.cursor()
query = "SELECT *  FROM art_cons_sourse limit 10"
cursorObject.execute(query)
   
myresult = cursorObject.fetchall()
   
for x in myresult:
    print(x)
  
# Disconnecting from the server
dataBase.close()