class User:
    def __init__(self, username, email, password):
        self._username = username
        self._email = email
        self._password = password

    def getUseranme(self):
        return self._username

    def getEmail(self):
        return self._email

    def getPassword(self):
        return self._password

    def setUsername(self, newUsername):
        self._username = newUsername

    def setEmail(self, newEmail):
        self._email = newEmail

    def setPassword(self, newPassword):
        self._password = newPassword

    def display_user_info(self):
        return f"Логин: {self._username}, Email: {self._email}"

    def validate_password(self):
        passord = input("Введите пароль: ")
        if passord == self._password:
            return "True"
        else:
            return "False"


user = User("HambaTheGreat", "Dan.Yermagambetov@gmail.com", "SpectrumY2023")
print(user.display_user_info())
print(user.validate_password())