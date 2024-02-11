from flask import url_for
from flask.testing import FlaskClient


def test_get_index_html(client: FlaskClient) -> None:
    response = client.get(url_for('index'))
    assert response.status_code == 200
    assert 'Home page' in response.data.decode('utf-8')


def test_get_signup_html(client: FlaskClient) -> None:
    response = client.get(url_for('user.signup'))
    assert response.status_code == 200
    assert 'Registration page' in response.data.decode('utf-8')


def test_post_signup(client, user_data_create):
    sign_up_data = user_data_create['sign_up_data']
    response = client.post(
        url_for('user.signup'),
        data={
            'login': sign_up_data['login'],
            'password': sign_up_data['password'],
            'confirm_password': sign_up_data['password'],
            'email': sign_up_data['email'],
        })
    assert response.status_code == user_data_create['result']['status_code']
    assert user_data_create['result']['html_content'] in response.data.decode('utf-8')


def test_get_login_html(client: FlaskClient) -> None:
    response = client.get(url_for('user.login'))
    assert response.status_code == 200
    assert 'Login page' in response.data.decode('utf-8')


def test_post_login(client, valid_user_data):
    user, user_data_dict = valid_user_data
    response = client.post(
        url_for('user.process_login'),
        data={
            'login': user_data_dict['login'],
            'password': user_data_dict['password'],
        })
    assert response.status_code == 302
    assert url_for('user.dashboard') in response.data.decode('utf-8')
