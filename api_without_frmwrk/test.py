import json

import mysql.connector

data_base = mysql.connector.connect(
    host="bwvzuhfivw9gtfcakuy4-mysql.services.clever-cloud.com",
    user="usa4j6o5j6rqqjzd",
    passwd="4juL9xuhE7CMF5YuWqJh",
    database="bwvzuhfivw9gtfcakuy4"
)

print("data_base: ", data_base)

# preparing a cursor object
cursorObject = data_base.cursor(dictionary=True)

query = "SELECT NAME, EMAIL,USERNAME,MOBILE FROM user"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)

data = json.dumps(myresult)
print("\n")
print("data:", data)
# disconnecting from server
data_base.close()


