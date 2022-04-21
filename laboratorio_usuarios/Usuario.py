class Usuario:
    def __init__(self, id_usuario = None, username = None, password = None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

    def __str__(self):
        return f'ID: {self._id_usuario}, Username: {self._username}, Password: {self._password}'

    @property
    def getId_usuario(self):
        return self._id_usuario

    @property
    def getUsername(self):
        return self._username
    @getUsername.setter
    def setUsernamer(self, username):
        self._username = username

    @property
    def getPassword(self):
        return self._password
    @getPassword.setter
    def setPassword(self, password):
        self._password = password

