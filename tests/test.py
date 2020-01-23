import requests
import random
from utils.test_get_token import test_get_token
import configparser


parser = configparser.ConfigParser()
parser.read('C:\\Users\\traxx\\PycharmProjects\\sandbox\\tests\\simple_config.ini')                                #подставить расположение файла simple config
REGISTRATION_URL = parser.get('suite_url\'s', 'registration_url')
AUTH_URL = parser.get('suite_url\'s', 'auth_url')

token = test_get_token()
random_email = random.randrange(100, 50000000, 1)
email = str(random_email) + 'fodz3@mail.com'
first_name = str(random_email) + 'testFirstName'
last_name = str(random_email) + 'testLastName'
password = "qweR1234"


def test_register_success():
    response = requests.post(REGISTRATION_URL, json={
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'password': password
    })
    assert 201 == response.status_code


def test_register_with_exist_email():
    response = requests.post(REGISTRATION_URL, json={
        'email': 'foo@bar.com',
        'first_name': first_name,
        'last_name': last_name,
        'password': password
    })
    assert 400 == response.status_code


def test_auth():
    response = requests.post(AUTH_URL, json={
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'password': password,
        'token': token
    })
    assert 200 == response.status_code
