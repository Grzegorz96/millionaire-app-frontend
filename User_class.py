# User Class for Global logged_in_user_info variable
class User:
    def __init__(self, active_flag, email, first_name, last_name, login, password, user_id, access_token,
                 refresh_token):
        self.active_flag = active_flag
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.password = password
        self.user_id = user_id
        self.access_token = access_token
        self.refresh_token = refresh_token
