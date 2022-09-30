### PYTHON BDD FRAMEWORK
----------------------------------------------------------------------
#### LOCAL SET UP
In order to run the automated test suite, please follow the steps described below:

1. You'll need python3, pip and MySql running on localhost to run this project

2. Run the command `pip install -r requirements.txt`

3. Create a `secrets.env.json` file on the root of the project with the following structure:
```
{
  "github_token": [YOUR_GITHUB_PERSONAL_ACCESS_TOKEN],
  "db_user" : [YOUR_LOCAL_MYSQL_USERNAME],
  "db_pass" : [YOUR_LOCAL_MYSQL_PASSWORD]
}
```

4. Run one of the commands below depending on which environment needs to be tested  
   - To execute the tests using the Test Runner (does not generate reports)  
     - `behave --no-capture`

#### MYSQL SetUp
- To set up MySQL locally run the following commands:
```
docker run -d -p 3306:3306 --name mysql-home -e MYSQL_ROOT_PASSWORD=some-pass -e MYSQL_DATABASE=tr3jo-db -e MYSQL_USER=some-user -e MYSQL_PASSWORD=some-pass mysql
docker exec -ti mysql-home bash
mysql -u root -p
SHOW DATABASES;
```
- Paste the entire content of scripts/queries.sql into the terminal and enter to execute
- Run the following commands:
```
UPDATE mysql.user SET host = ‘%’ WHERE user=’root’;
GRANT ALL PRIVILEGES ON APIDevelop.* to 'some-user'@'%';
FLUSH PRIVILEGES;
```

- To test the MySQL connection run: `python utilities/main.py`