import configparser

config = configparser.RawConfigParser()

config.read(".\\Configuration\\config.ini")


class ReadConfig:

    @staticmethod
    def get_login_url():
        login_url = config.get('application url', 'login_url')
        return login_url

    @staticmethod
    def get_username():
        username = config.get('login data', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('login data', 'password')
        return password

