from datetime import datetime

import peewee as pw

db = pw.SqliteDatabase('users.db')


class BaseModel(pw.Model):
    created_at = pw.DateTimeField(default=datetime.now)

    class Meta:
        database = db


class User(BaseModel):
    email = pw.CharField(unique=True)
    password = pw.CharField()
    username = pw.CharField()

    def __repr__(self):
        fields = (
            "User("
                f"username={self.username},"
                f"email={self.email},"
                f"password={self.password}"
            ")"
        )

        return fields

    def __str___(self):
        return self.__repr__()

    @staticmethod
    def get_all():
        users = User.select().namedtuples()
        all = {
            user.id: {
                'username': user.username,
                'email': user.email,
                'password': user.password,
            }
            for user in users
        }

        return all

    def update_all(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

        self.save()
