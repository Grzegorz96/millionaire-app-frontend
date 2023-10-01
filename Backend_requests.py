# Modules import.
from requests import get, post, patch, delete, RequestException, Response
# Module Config for global variables.
import Config


def get_questions_request():
    """The function responsible for sending a request to download questions from the database."""
    # Creating endpoint and calling GET method on this endpoint.
    try:
        url = "http://Grzegorz96.pythonanywhere.com/questions"
        response = get(url)
    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from GET method.
    else:
        return response


def check_for_registration_request(login, email):
    """The function responsible for sending a request to check the availability of login and email in the database."""
    # Creating endpoint, request_body and calling GET method on this endpoint.
    try:
        url = "http://Grzegorz96.pythonanywhere.com/users/register/check-data"
        request_body = {
            "login": login,
            "email": email
        }
        response = get(url, json=request_body)
    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from GET method.
    else:
        return response


def send_activation_number_request(email):
    """The function responsible for sending a request to send activation number to user's email."""
    # Creating endpoint, request_body and calling POST method on this endpoint.
    try:
        url = "http://Grzegorz96.pythonanywhere.com/users/send-activation-number"
        request_body = {"email_receiver": email}
        response = post(url, json=request_body)
    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from POST method.
    else:
        return response


def registration_user_request(first_name, last_name, login, password, email):
    """The function responsible for sending a request to add user's data to the database."""
    # Creating endpoint, request_body and calling POST method on this endpoint.
    try:
        url = "http://Grzegorz96.pythonanywhere.com/users/register"
        request_body = {
            "first_name": first_name,
            "last_name": last_name,
            "login": login,
            "password": password,
            "email": email
        }
        response = post(url, json=request_body)
    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from POST method.
    else:
        return response


def login_user_request(login, password):
    """The function responsible for sending a request to get user's ID and JWT tokens from database (logging in)."""
    # Creating endpoint, request_body and calling GET method on this endpoint.
    try:
        url = "http://Grzegorz96.pythonanywhere.com/users/login"
        request_body = {
            "login": login,
            "password": password
        }
        response = get(url, json=request_body)
    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from GET method.
    else:
        return response


def get_user_info_request(user_id, access_token, refresh_token):
    """The function responsible for sending a request to get user's data from database, using ID and JWT tokens."""
    # Creating endpoint, headers, subresource and calling GET method on this endpoint.
    try:
        url = f"http://Grzegorz96.pythonanywhere.com/users/{user_id}"
        headers = {
            "access-token": access_token,
            "refresh-token": refresh_token
        }
        response = get(url, headers=headers)
    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from GET method.
    else:
        return response


def get_best_scores_request(limit):
    """The function responsible for sending a request to get scores from database."""
    # Creating endpoint.
    try:
        url = "http://Grzegorz96.pythonanywhere.com/scores"
        # If parameter limit != None then HTTP parameter limit is creating and calling GET method with this parameter.
        if limit:
            params = {"limit": limit}
            response = get(url, params=params)
        # Else calling GET method without parameters.
        else:
            response = get(url)
    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from GET method.
    else:
        return response


def send_score_request(points):
    """The function responsible for sending a request to add user's score to the database, using JWT tokens."""
    # Creating endpoint, headers, request_body and calling POST method on this endpoint.
    try:
        url = "http://Grzegorz96.pythonanywhere.com/scores"
        headers = {
            "access-token": Config.logged_in_user_info.access_token,
            "refresh-token": Config.logged_in_user_info.refresh_token
        }
        request_body = {
            "user_id": Config.logged_in_user_info.user_id,
            "points": points
        }
        response = post(url, headers=headers, json=request_body)
    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from POST method.
    else:
        return response


def update_user_request(request_body):
    """The function responsible for sending a request to update user's data in the database, using JWT tokens."""
    # Creating endpoint, headers, subresource and calling PATCH method on this endpoint.
    try:
        url = f"http://Grzegorz96.pythonanywhere.com/users/{Config.logged_in_user_info.user_id}"
        headers = {
            "access-token": Config.logged_in_user_info.access_token,
            "refresh-token": Config.logged_in_user_info.refresh_token
        }

        response = patch(url, headers=headers, json=request_body)
    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from PATCH method.
    else:
        return response


def delete_user_request():
    """The function responsible for sending a request to delete user's data from the database, using JWT tokens."""
    # Creating endpoint, headers, subresource and calling DELETE method on this endpoint.
    try:
        url = f"http://Grzegorz96.pythonanywhere.com/users/{Config.logged_in_user_info.user_id}"
        headers = {
            "access-token": Config.logged_in_user_info.access_token,
            "refresh-token": Config.logged_in_user_info.refresh_token
        }

        response = delete(url, headers=headers)
    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from DELETE method.
    else:
        return response


def add_questions_request(request_body):
    """The function responsible for sending a request to add question to the database, using JWT tokens."""
    #  Creating endpoint, headers and calling POST method on this endpoint.
    try:
        url = "http://Grzegorz96.pythonanywhere.com/questions"
        headers = {
            "access-token": Config.logged_in_user_info.access_token,
            "refresh-token": Config.logged_in_user_info.refresh_token
        }

        response = post(url, json=request_body, headers=headers)
    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from POST method.
    else:
        return response
