import json

import psycopg2
# from botocore.exceptions import ClientError
from psycopg2.extras import RealDictCursor

host = 'mf-db-instance.c730haw9dwg6.us-east-1.rds.amazonaws.com'
database = 'testdb'
user = 'postgres'
password = 'postgres'


def lambda_handler(event, context):
    # TODO implement
    try:
        print("event:", event)
        response = {}

        # db_config = get_db_config()
        # print("db_config : ", db_config)
        # print("******************", db_config["host"])
        print("******************", host)
        print("******************", database)
        print("******************", user)
        print("******************", password)

        # create sql conenction object
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        # conn = psycopg2.connect(
        #     host=db_config["host"],
        #     database=db_config["database"],
        #     user=db_config["user"],
        #     password=db_config["password"]
        # )
        print("conn ----:", conn)

        cur = conn.cursor(cursor_factory=RealDictCursor)
        print("cur ----:", cur)

        query_data = f"select * from user_info;"
        print("QUERY : ", query_data)
        cur.execute(query_data)

        row = cur.fetchall()
        # row = dict(list(row))
        cur.close()
        conn.close()

        # response["body"] = json.dumps({"body": row}, default=str)
        # # print("response :", response)
        # return response
        print(row)
        return response


    except ClientError as e:
        response["body"] = json.dumps({"message": e.response['Error']['Message']})
        return response



def get_db_config():
    # tenant specific postgres credential
    # host = 'mf-db-instance.c730haw9dwg6.us-east-1.rds.amazonaws.com'
    host = 'mf-db-instance.c730haw9dwg6.us-east-1.rds.amazonaws.com'
    database = 'testdb'
    user = 'postgres'
    password = 'postgres'

    dateformat_default = "%Y-%m-%d"
    dateformat = dateformat_default

    # print(dateformat)
    return {
        "host": host,
        "database": database,
        "user": user,
        "password": password
        # "dateformat": dateformat
    }


#
# def lambda_handler(event, context):
#     # TODO implement
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda!')
#     }


def test():
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    print(conn)

    cur = conn.cursor(cursor_factory=RealDictCursor)
    print("cur ----:", cur)

    query_data = f"select * from user_info;"
    print("QUERY : ", query_data)
    cur.execute(query_data)

    row = cur.fetchall()

    # print("Fetched get user : ", row)
    # row = list(row)
    cur.close()
    conn.close()
    print(row)


test()
