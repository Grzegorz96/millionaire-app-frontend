from requests import get, post, RequestException, Response


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
        request_body = {"login": login, "email": email}
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
        headers = {"access-token": access_token, "refresh-token": refresh_token}
        response = get(url, headers=headers)

    except RequestException:
        response = Response()
        response.status_code = 404
        return response

    else:
        return response


def get_best_scores_request():
    try:
        url = f"http://localhost:3000/scores"
        params = {"limit": 10}
        response = get(url, params=params)

    except RequestException:
        response = Response()
        response.status_code = 404
        return response

    else:
        return response
