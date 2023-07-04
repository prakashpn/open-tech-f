import pandas as pd
from sqlalchemy.event import listen
from sqlalchemy.orm import Session


def data_frame_query(make_row, query):
    """
    Takes a sqlalchemy query and a list of columns, returns a dataframe.
    """

    return pd.DataFrame([make_row(x) for x in query])


def data_frame_list(data_list):
    return pd.DataFrame(data_list)


class CrudRepository:
    def __init__(self, session):
        """

        :type session: Session
        """
        self.session = session

    def close_session(self):
        self.session.close()

    def limit_query(self, query, page=0, page_size=None):
        listen(query, 'before_compile', self.apply_limit(page, page_size), retval=True)

        return query

    def apply_limit(self, page, page_size):
        def wrapped(query):
            if page_size:
                query = query.limit(page_size)
                if page:
                    offset = page * page_size
                    query = query.offset(offset)
            return query

        return wrapped

    def ql(self, query, page=0, page_size=None):

        if page_size:
            query = query.limit(page_size)
        if page:
            query = query.offset(page * page_size)
        return query
