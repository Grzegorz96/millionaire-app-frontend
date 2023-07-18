# Modules import.
from requests import get, post, patch, delete, RequestException, Response
# Module Config for global variables.
import Config


# Request function for getting question.
def get_questions_request():
    # Creating endpoint and calling GET method on this endpoint.
    try:
        url = "http://localhost:3000/questions"
        response = get(url)
    # If cant connect with endpoint, making response object with 404 status code and return response.
    except RequestException:
        response = Response()
        response.status_code = 404
        return response
    # If everything ok from frontend then just return the response from GET method.
    else:
        return response


# Request function for checking info for registration with transferred login and email form Functions module.
def check_for_registration_request(login, email):
    # Creating endpoint, request_body and calling GET method on this endpoint.
    try:
        url = "http://localhost:3000/users/register/check-data"
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


# Request function for sending activation number with email parameter from Functions module.
def send_activation_number_request(email):
    # Creating endpoint, request_body and calling POST method on this endpoint.
    try:
        url = "http://localhost:3000/users/send-activation-number"
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


#  Request function for registration user with parameters transferred from Functions.
def registration_user_request(first_name, last_name, login, password, email):
    # Creating endpoint, request_body and calling POST method on this endpoint.
    try:
        url = "http://localhost:3000/users/register"
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


# Request function for login user with login and password parameters transferred from Functions.
def login_user_request(login, password):
    # Creating endpoint, request_body and calling GET method on this endpoint.
    try:
        url = "http://localhost:3000/users/login"
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


# Request functon for getting user info with user_id, access_token and refresh_token transferred from Functions.
def get_user_info_request(user_id, access_token, refresh_token):
    # Creating endpoint, headers, subresource and calling GET method on this endpoint.
    try:
        url = f"http://localhost:3000/users/{user_id}"
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


# Request function for getting best scores with limit parameter transferred from Functions.
def get_best_scores_request(limit):
    # Creating endpoint.
    try:
        url = "http://localhost:3000/scores"
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


# Request function for sending score with points parameter.
def send_score_request(points):
    # Creating endpoint, headers, request_body and calling POST method on this endpoint.
    try:
        url = "http://localhost:3000/scores"
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


# Request function for updating user with already created request body from Functions.
def update_user_request(request_body):
    # Creating endpoint, headers, subresource and calling PATCH method on this endpoint.
    try:
        url = f"http://localhost:3000/users/{Config.logged_in_user_info.user_id}"
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


# Request function for deleting user.
def delete_user_request():
    # Creating endpoint, headers, subresource and calling DELETE method on this endpoint.
    try:
        url = f"http://localhost:3000/users/{Config.logged_in_user_info.user_id}"
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


# Request function for adding questions with already created request body from Functions.
def add_questions_request(request_body):
    #  Creating endpoint, headers and calling POST method on this endpoint.
    try:
        url = "http://localhost:3000/questions"
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
