import matplotlib.pyplot as plt
import sqlite3


years = []
co2 = []
temp = []

connection=sqlite3.connect("week8test\WS8\climate.db")#from local 
cursor=connection.cursor()
cursor.execute("SELECT * FROM ClimateData")
result=cursor.fetchall()
for row in result:
    #print(row[0])#year
    years.append( row[0])
    co2.append(row[1])
    temp.append(row[2])

print(years)
print(co2)
print (temp)



plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 
plt.show()



