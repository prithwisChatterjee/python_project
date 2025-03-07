# A Test Connection Page
import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="",
  database = "testDb"
)
cursorObject = dataBase.cursor()
query = "SELECT *  FROM art_cons_sourse limit 10"
cursorObject.execute(query)
   
myresult = cursorObject.fetchall()
   
for x in myresult:
    print(x)
  
# Disconnecting from the server
dataBase.close()