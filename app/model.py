import peewee as pw

db = pw.SqliteDatabase('users.db')

class BaseModel(pw.Model):
    class Meta:
        database = db


class User(BaseModel):
    email = pw.CharField(unique=True)
    password = pw.CharField()
    username = pw.CharField()

    def __repr__(self):
        return f"""
            User(
                username={self.username},
                email={self.email},
                password={self.password}
            )
        """

    def __str___(self):
        return self.__repr__()
