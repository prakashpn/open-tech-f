import json

import psycopg2
from botocore.exceptions import ClientError
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
        body_data = json.loads(event["body"])
        # print("body_data :", (body_data))

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
        print("conn ----:", conn)

        check_data = get_data(conn, body_data["MOBILE"])
        print("Check _____", check_data)
        if check_data:
            response["body"] = json.dumps({"Message": "Mobile Number Already Present"}, default=str)
            return response

        cur = conn.cursor(cursor_factory=RealDictCursor)
        print("cur ----:", cur)

        insert_query = f"""INSERT INTO user_info 
                                      ("NAME","EMAIL","USERNAME","MOBILE")
                                      VALUES
                                      ('{body_data["NAME"]}','{body_data["EMAIL"]}',
                                      '{body_data["USERNAME"]}','{body_data["MOBILE"]}')"""

        print("QUERY : ", insert_query)
        cur.execute(insert_query)

        cur.close()
        conn.commit()
        # conn.close()

        response["body"] = json.dumps({"Message": "User Inserted Successfully"}, default=str)
        return response


    except Exception as e:
        print("e------------------", e)
        response["body"] = json.dumps({"message": e.response['Error']['Message']})
        return response

    # except ClientError as e:
    #     print("e------------------",e)
    #     response["body"] = json.dumps({"message": e.response['Error']['Message']})
    #     return response


def get_data(conn, phone):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    check_phone = f"""select * from user_info where "MOBILE"={phone};"""
    print("QUERY : ", check_phone)
    cur.execute(check_phone)
    row = cur.fetchone()
    # if row:
    cur.close()
    return row
