class User:
    """User class, after the user logs in, the retrieved data will be assigned to the fields of the user object."""
    def __init__(self, active_flag, email, first_name, last_name, login, password, user_id, access_token,
                 refresh_token):
        """Constructor for the User class."""
        self.active_flag = active_flag
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.password = password
        self.user_id = user_id
        self.access_token = access_token
        self.refresh_token = refresh_token
