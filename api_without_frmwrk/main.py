import http.server
import json
import socketserver

import mysql.connector

from api_without_frmwrk.random_string import randomString

PORT = 8000


class MyHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.path = "index.html"
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

        if self.path == "/user":
            data_base = mysql.connector.connect(
                host="bwvzuhfivw9gtfcakuy4-mysql.services.clever-cloud.com",
                user="usa4j6o5j6rqqjzd",
                passwd="4juL9xuhE7CMF5YuWqJh",
                database="bwvzuhfivw9gtfcakuy4"
            )
            # preparing a cursor object
            cursorObject = data_base.cursor(dictionary=True)

            query = f"SELECT USER_ID, NAME, EMAIL, GEN_DATE, STATUS, USERNAME, MOBILE, IMAGE FROM user"
            cursorObject.execute(query)

            myresult = cursorObject.fetchall()
            data_base.close()

            # - response -
            self.send_response(200)
            self.send_header('Content-type', 'text/json')
            self.end_headers()
            output_data = myresult
            output_json = json.dumps(output_data, default=str)

            self.wfile.write(output_json.encode('utf-8'))

    def do_POST(self):
        # - request -
        if self.path == "/post":

            content_length = int(self.headers['Content-Length'])
            # print('content_length:', content_length)

            if content_length:
                input_json = self.rfile.read(content_length)
                print("input_json------", input_json)

                # print("input_json------", input_json["NAME"])
                input_data = json.loads(input_json)
                print("input_json NAME------", input_data["NAME"])
                print("input_json EMAIL------", input_data["EMAIL"])
                print("input_json USERNAME------", input_data["USERNAME"])
                print("input_json MOBILE------", input_data["MOBILE"])


            else:
                input_data = None

            print("----------", input_data)
            if input_data:
                try:
                    password = randomString(10)
                    data_base = mysql.connector.connect(
                        host="bwvzuhfivw9gtfcakuy4-mysql.services.clever-cloud.com",
                        user="usa4j6o5j6rqqjzd",
                        passwd="4juL9xuhE7CMF5YuWqJh",
                        database="bwvzuhfivw9gtfcakuy4"
                    )
                    # preparing a cursor object
                    cursorObject = data_base.cursor(dictionary=True)

                    #  check phone no avail or not
                    get_query = f"""SELECT USER_ID, NAME, EMAIL, GEN_DATE, STATUS, USERNAME, MOBILE, IMAGE FROM user WHERE MOBILE={input_data["MOBILE"]}"""
                    cursorObject.execute(get_query)

                    result = cursorObject.fetchone()
                    if result:
                        print("Phone Present")
                        self.send_response(409)
                        self.send_header('Content-type', 'text/json')
                        self.end_headers()
                        output_data = {'message': 'Phone No Already Registered'}
                        output_json = json.dumps(output_data)
                        self.wfile.write(output_json.encode('utf-8'))
                    else:

                        insert_query = f"""INSERT INTO user (NAME, EMAIL, USERNAME, MOBILE, PASSWORD) 
                                            VALUES ('{input_data['NAME']}',"{input_data['EMAIL']}",' {input_data['USERNAME']}', {input_data['MOBILE']},'{password}')"""
                        print("insert_query :---", insert_query)
                        cursorObject.execute(insert_query)
                        data_base.commit()
                        data_base.close()

                        self.send_response(200)
                        self.send_header('Content-type', 'text/json')
                        self.end_headers()
                        output_data = {'status': 'OK', 'result': 'User Inserted Successfully'}
                        output_json = json.dumps(output_data)

                        self.wfile.write(output_json.encode('utf-8'))
                except Exception as e:
                    print("e-------", e)
                    self.send_response(500)
                    self.send_header('Content-type', 'text/json')
                    self.end_headers()
                    output_data = {'message': 'Something went wrong'},
                    output_json = json.dumps(output_data)
                    self.wfile.write(output_json.encode('utf-8'))


Handler = MyHandler

# httpd = HTTPServer(("localhost", 8080), Handler)
# httpd.serve_forever()
myserver = socketserver.TCPServer(("localhost", PORT), Handler)
print(f"Starting http://localhost:{PORT}")
myserver.serve_forever()

# try:
#     with socketserver.TCPServer(("", PORT), Handler) as httpd:
#         print(f"Starting http://localhost:{PORT}")
#         httpd.serve_forever()
# except KeyboardInterrupt:
#     print("Stopping by Ctrl+C")
#     httpd.server_close()  # to resolve problem `OSError: [Errno 98] Address already in use`
