from config import *
from utilities.resources import *

config = get_config()

base_url = config['API']['host']
print(f'{base_url}{ApiResources.addBook}')

stringFormat = "Base URL: %s"
tupleVar = (base_url,)
print(stringFormat % tupleVar)

db_connection = get_db_cnx()

print(db_connection.is_connected())

db_streamline = db_connection.cursor()
db_streamline.execute("SELECT * from CustomerInfo")

# This first row will be REMOVED from the stream line queue
print(db_streamline.fetchone())
# Rest of the rows on the stream line
query_output = db_streamline.fetchall()

print(query_output)
print(query_output[2])
print(query_output[2][0])

update_info = "update CustomerInfo set Location = %s where CourseName = %s"
new_data = ('MX', 'Jmeter')
db_streamline.execute(update_info, new_data)
db_connection.commit()

db_streamline.close()
db_connection.close()

