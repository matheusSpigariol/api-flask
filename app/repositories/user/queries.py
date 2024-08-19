from app.interfaces.db_connection_interface import DbConnectionInterface

def get_user(user_id):
    sql = """
        SELECT
            *
        FROM
            users
        WHERE
            id = %(user_id)s
    """
    mapping = {"user_id": user_id}
    return DbConnectionInterface().fetch_one(sql, mapping)
