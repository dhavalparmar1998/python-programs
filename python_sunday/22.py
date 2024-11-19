import mysql.connector
import requests


class config:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "pythonsunday"

class connect(config):
    def dbconnect(self):
        self.dbconn = mysql.connector.connect(
             host =self.host,
             user =self.user,
             passwd =self.password,
             database = self.database
 
        )        
        return self.dbconn       
    
class crudoperation(connect):
    def insertdata(self, username, userplace, userage):
        print("inserting data")
        print(username,userplace,userage) 

        sql = "INSERT INTO users (name, place, age) VALUES (%s, %s, %s)"
        val = (username,userplace,userage)

        databaseconnection = self.dbconnect()
        cursorobject = databaseconnection.cursor()
        cursorobject.execute(sql, val)
        databaseconnection.commit()   

    def selectdata(self):
        databaseconnection = self.dbconnect()
        cursorobject = databaseconnection.cursor()

        query = "SELECT name,age,place FROM users"
        cursorobject.execute(query)
   
        myresult = cursorobject.fetchall()
        return myresult
    
    def update(self):
        pass

    def delete(self):
        pass


obj = crudoperation()

# obj.insertdata("rohit","thane",22)
# obj.insertdata("manish","parel",22)


ans = obj.selectdata()
print(ans)


# response = requests.get("https://fakestoreapi.com/users/1")
# results = response.json()

# print(results, type(results))
# print(results["username"])
# obj.insertdata(results["username"],"parel",23)
   

