# ForYou

# crete virtual env

  ```sh
    virtualenv -p python3.8 env 
  ```

# Active virtual env

 ```sh
    source env/bin/activate
  ```

# install required module

 ```sh
    pip install -r requirements.txt
  ```

```commandline
    used local MySql DB
    update acordingly
    
    sql import file is included in /sql_import_file
```

```run the flask app -->flask run

        get_user API :GET   http://localhost:8080/rest/user/user-list
        insert user  :POST  http://localhost:8080/rest/user/insert
                            payload {
                                        "NAME":"absc",
                                        "EMAIL":"abac@gmail.com",
                                        "USERNAME":"abc",
                                        "MOBILE":1234367809
                                    }
        for imgae upload:POST   http://localhost:8080/open-tech-image
            will get the Web Screen then put the user Id and image

```
