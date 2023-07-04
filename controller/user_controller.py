'''
DOC:            04/06/2023
Created By:     Prakash
Purpose:        get all ,Insert and update user
'''
import os

from flask import jsonify, Blueprint, request, Response
from werkzeug.utils import secure_filename

from base_util import image_dir
from database.db_config import close_session, create_session, User, Image
from json_serialize.json_util import UserJson
from repository.user_repository import UserRepository
from service.user_service import UserService
from util.random_string import allowed_file

user_app = Blueprint('user', __name__)

'''
Name:       view_user_list()
DOC:        04/07/2023
Method:     GET
Parameters: 
Purpose:    Used to get all user from user table
Return:     [List]  response of success/Failure
'''


@user_app.route('/user-list', methods=['GET'])
def view_user_list():
    """
    return:    It will give you user list present in User Table
    """
    try:
        session_con, con = create_session()
        datas = UserRepository(session_con).find_all()
        json_data = UserJson.get_list(datas, exclude=["PASSWORD", "USERNAME"])
        close_session(session_con, con)
        response = jsonify(json_data)
        return response

    except Exception as e:
        return e


'''
Name:       insert_user()
DOC:        04/07/2023
Method:     POST
Purpose:    Used to create/insert new record in the user table
Return:     message:  response of success/Failure
'''


@user_app.route('/insert', methods=['POST'])
def insert_user():
    """

    :return: success message or error if found
    :rtype:
    """
    session_con, con = create_session()
    data = request.json
    try:
        response = UserService(session_con).insert_user(data)
        session_con.commit()
        close_session(session_con, con)
        return response
    except Exception as e:
        return e


'''
Name:       insert_user()
DOC:        04/07/2023
Method:     POST
Purpose:    Used to create/insert new record in the user table
Return:     message:  response of success/Failure
'''


@user_app.route('/upload-image', methods=['POST'])
def upload_image():
    session_con, con = create_session()
    file = request.files['pic']
    user_id = request.form['userId']
    print(file)
    print(user_id)
    try:
        if user_id:
            if file and allowed_file(file.filename):
                file_name = secure_filename(file.filename)
                print(file_name)
                file_name = user_id + "_" + file_name
                file.save(os.path.join(image_dir, file_name))
                response = UserService(session_con).insert_user_image(file_name, user_id)
                session_con.commit()
                close_session(session_con, con)
                return response
            else:
                return jsonify({"message": "Extension does not match"})
        else:
            return jsonify({"message": "Please share the User Id"})
    except Exception as e:
        print(e)
