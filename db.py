import os

import MySQLdb


class MyDB:
    cursor = None

    @classmethod
    def init_cursor(cls):
        """
        Get the cursor for the database
        :return: cursor for the database
        """
        if cls.cursor is None:
            cls.connection = MySQLdb.connect(
                database=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                passwd=os.getenv('DB_PASSWORD'),
                host=os.getenv('DB_HOST'),
                port=os.getenv('DB_PORT')
            )

            cls.cursor = cls.connection.cursor()

    @classmethod
    def __commit(cls):
        """
        Commit the changes to the database
        """
        cls.cursor.connection.commit()

    @classmethod
    def create_ascii_art_result(cls, result, created_at, upload_image_id, compress_level, is_public):
        # Example INSERT statement
        insert_query = "INSERT INTO table (val1, val2, val3, val4, val5) VALUES (%s, %s, %s, %s, %s)"
        data = (result, created_at, upload_image_id, compress_level, is_public)

        # Execute the INSERT statement
        cls.cursor.execute(insert_query, data)

        # Commit the transaction to make the changes permanent
        cls.__commit()
