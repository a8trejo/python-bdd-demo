import os.path
import configparser
import json
import mysql.connector
from mysql.connector import Error

def get_config():
    config = configparser.ConfigParser()
    config.read('properties.ini')

    if os.path.exists("secrets.env.json"):
        secrets_file = open("secrets.env.json")
        secrets_json = json.load(secrets_file)
        secrets_file.close()
        config['SQL Properties']['user'] = secrets_json['db_user']
        config['SQL Properties']['pass'] = secrets_json['db_pass']
        config['API']['github_token'] = secrets_json['github_token']
        return config
    else:
        return config

def get_db_cnx():
    db_config = {
        "host": get_config()['SQL Properties']['host'],
        "database": get_config()['SQL Properties']['db_name'],
        "user": get_config()['SQL Properties']['user'],
        "password": get_config()['SQL Properties']['pass']
    }

    try:
        # db_connection = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_pass)
        db_connection = mysql.connector.connect(**db_config)
        if db_connection.is_connected():
            print("DB Connection Successful")
            return db_connection
        else:
            print("DB Connection failed")
    except Error as e:
        print(e)
