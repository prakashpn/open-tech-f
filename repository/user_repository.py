from datetime import datetime

from database.db_config import User, Image
from repository.curd_repository import CrudRepository


class UserRepository(CrudRepository):

    def __init__(self, session):
        self.session = session

    def find_all(self):
        """
        find all data from database from User table
        :return: list of User
        :rtype: User (sqlalchemy automap object)
        """
        query = self.session.query(User).all()
        return query

    def insert_user(self, user):
        user.GEN_DATE = datetime.now()
        user.STATUS = "Y"
        self.session.add(user)
        self.session.flush()
        self.session.refresh(user)
        return user

    def upload_image(self, image):
        # image.GEN_DATE = datetime.now()
        # image.STATUS = "Y"
        self.session.add(image)
        self.session.flush()
        self.session.refresh(image)
        return image

    def find_by_id(self, USER_ID):
        return self.session.query(User).get(USER_ID)

    def find_by_email(self, EMAIL):
        return self.session.query(User).filter(User.EMAIL == EMAIL).first()

    def find_by_mobile(self, MOBILE):
        return self.session.query(User).filter(User.MOBILE == MOBILE).first()

    def get_image(self, id):
        # Image.query.filter_by(IMAGE_ID=id).first()
        return self.session.query(Image).filter(Image.IMAGE_ID == id).first()
