import requests
import random



def auth():
    random_email = random.randrange(100, 50000000, 1)
    email = str(random_email) + 'fodz3@mail.com'
    print(email)
    first_name = str(random_email) + 'testFirstName'
    last_name = str(random_email) + 'testLastName'
    password = "qweR1234"
    response = requests.post('https://api.newbookmodels.com/api/v1/auth/client/signup/', json={
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'password': password
    })
    b = response.json()
    token = b['token_data']['token']
    print(token)
    print(response.json())
    assert 201 == response.status_code



    response = requests.post('https://api.newbookmodels.com/api/v1/auth/signin/', json={'email': email,
                                                                                       'password': password,
                                                                                       'token': token})
    print(response.json())
    assert 200 == response.status_code

auth()