from requests import get, post, patch, delete, RequestException, Response
import Config


def get_questions_request():
    try:
        url = "http://localhost:3000/questions"
        response = get(url)

    except RequestException:
        response = Response()
        response.status_code = 404
        return response

    else:
        return response


def check_for_registration_request(login, email):
    try:
        url = "http://localhost:3000/users/register/check-data"
        request_body = {
            "login": login,
            "email": email
        }
        response = get(url, json=request_body)

    except RequestException:
        response = Response()
        response.status_code = 404
        return response

    else:
        return response


def send_activation_number_request(email):
    try:
        url = "http://localhost:3000/users/send-activation-number"
        request_body = {"email_receiver": email}
        response = post(url, json=request_body)

    except RequestException:
        response = Response()
        response.status_code = 404
        return response

    else:
        return response


def registration_user_request(first_name, last_name, login, password, email):
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

    except RequestException:
        response = Response()
        response.status_code = 404
        return response

    else:
        return response


def login_user_request(login, password):
    try:
        url = "http://localhost:3000/users/login"
        request_body = {
            "login": login,
            "password": password
        }
        response = get(url, json=request_body)

    except RequestException:
        response = Response()
        response.status_code = 404
        return response

    else:
        return response


def get_user_info_request(user_id, access_token, refresh_token):
    try:
        url = f"http://localhost:3000/users/{user_id}"
        headers = {
            "access-token": access_token,
            "refresh-token": refresh_token
        }
        response = get(url, headers=headers)

    except RequestException:
        response = Response()
        response.status_code = 404
        return response

    else:
        return response


def get_best_scores_request(limit):
    try:
        url = "http://localhost:3000/scores"
        if limit:
            params = {"limit": limit}
            response = get(url, params=params)
        else:
            response = get(url)

    except RequestException:
        response = Response()
        response.status_code = 404
        return response

    else:
        return response


def send_score_request(points):
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

    except RequestException:
        response = Response()
        response.status_code = 404
        return response

    else:
        return response


def update_user_request(request_body):
    try:
        url = f"http://localhost:3000/users/{Config.logged_in_user_info.user_id}"
        headers = {
            "access-token": Config.logged_in_user_info.access_token,
            "refresh-token": Config.logged_in_user_info.refresh_token
        }

        response = patch(url, headers=headers, json=request_body)

    except RequestException:
        response = Response()
        response.status_code = 404
        return response

    else:
        return response


def delete_user_request():
    try:
        url = f"http://localhost:3000/users/{Config.logged_in_user_info.user_id}"
        headers = {
            "access-token": Config.logged_in_user_info.access_token,
            "refresh-token": Config.logged_in_user_info.refresh_token
        }

        response = delete(url, headers=headers)

    except RequestException:
        response = Response()
        response.status_code = 404
        return response

    else:
        return response


def add_questions_request(request_body):
    try:
        url = "http://localhost:3000/questions"
        headers = {
            "access-token": Config.logged_in_user_info.access_token,
            "refresh-token": Config.logged_in_user_info.refresh_token
        }

        response = post(url, json=request_body, headers=headers)

    except RequestException:
        response = Response()
        response.status_code = 404
        return response

    else:
        return response
