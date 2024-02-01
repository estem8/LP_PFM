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
    response = client.post(
        url_for('user.signup'),
        data={
            'login': user_data_create['login'],
            'password': user_data_create['password'],
            'confirm_password': user_data_create['password'],
            'email': user_data_create['email'],
        })
    assert response.status_code == 302
    assert '<a href="/users/dashboard">/users/dashboard</a>' in response.data.decode('utf-8')


def test_get_login_html(client: FlaskClient) -> None:
    response = client.get(url_for('user.login'))
    assert response.status_code == 200
    assert 'Login page' in response.data.decode('utf-8')


def test_post_login(client, user_data):
    user, user_data_dict = user_data
    response = client.post(
        url_for('user.process_login'),
        data={
            'login': user_data_dict['login'],
            'password': user_data_dict['password'],
        })
    assert response.status_code == 302
    assert '<a href="/users/dashboard">/users/dashboard</a>' in response.data.decode('utf-8')
