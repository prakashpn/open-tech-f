from flask import jsonify

from database.db_config import User, Image
from repository.user_repository import UserRepository
from util.random_string import randomString


class UserService():
    def __init__(self, session):
        self.session = session

    def insert_user(self, data):
        checkEmail = UserRepository(self.session).find_by_mobile(data.get("MOBILE"))
        if checkEmail is None:
            user = User()
            user.NAME = data.get("NAME")
            user.EMAIL = data.get("EMAIL")
            user.MOBILE = data.get("MOBILE")
            user.USERNAME = data.get("USERNAME")
            user.PASSWORD = randomString(10)
            UserRepository(self.session).insert_user(user)
            # return user
            return jsonify({"message": "User Inserted successfully"})
        if checkEmail is not None:
            return jsonify({"message": "Mobile Already Present"})

    def insert_user_image(self, file_name, user_id=1):
        user = UserRepository(self.session).find_by_id(user_id)
        if user is not None:
            user.IMAGE = file_name
            UserRepository(self.session).insert_user(user)
            return jsonify({"message": "Image Uploaded successfully"})
        if user is None:
            return jsonify({"message": "NO User Available"})

    def upload_image(self, data, filename, mimetype):
        image = Image()
        image.IMAGE = data.read()
        image.NAME = filename
        image.MIMETYPE = mimetype
        UserRepository(self.session).upload_image(image)
        return "image"
