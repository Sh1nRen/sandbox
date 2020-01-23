import requests
import random


def test_get_token():
    random_email = random.randrange(100, 50000000, 1)
    email = str(random_email) + 'fodz3@mail.com'
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
    assert 201 == response.status_code
    return token

# {"user":
#     {"id": "1d7091f9-299e-4dfc-93d8-bd4ee11e5139",
#      "type": "client",
#      "status": "pending",
#      "payment_method_connected": false,
#      "is_staff": false,
#      "email_verified": false,
#      "client_profile":
#          {"id": "8e3cd887-f09d-43f8-91eb-9994099ade89",
#           "facebook_followers": null,
#           "instagram_followers": null,
#           "has_invite": false,
#           "company_website": null,
#           "company_name": null,
#           "company_description": null,
#           "referral": null,
#           "phone_number": null,
#           "is_sms_enabled": true,
#           "location_latitude": null,
#           "location_longitude": null,
#           "location_name": null,
#           "location_city_name": null,
#           "location_admin1_code": null,
#           "location_timezone": null,
#           "company_address": null,
#           "industry": null,
#           "twitter_followers": null,
#           "youtube_followers": null},
#      "has_password": true,
#      "avatar": null,
#      "email": "35495441fodzxc123@b1211aaaaxr.com",
#      "first_name": "test",
#      "last_name": "test"},
# "token_data": {"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1Nzk1OTU5NzksInVzZXJfaWQiOiIxZDcwOTFmOS0yOTllLTRkZmMtOTNkOC1iZDRlZTExZTUxMzkiLCJleHAiOjE1ODIxODc5Nzl9.L5pxEcM-qKiBKYWjQ9K0_02kpSpgFNu89EmV5rFphvo", "token_refresh_expires": "2020-02-20T08:39:39.000000Z", "firebase_token": "eyJhbGciOiAiUlMyNTYiLCAidHlwIjogIkpXVCIsICJraWQiOiAiOTI3NzhkYjE0NzIyNzg3OTkzM2FjZmI1MDZlOTQzZWMwOGUyZmY1MCJ9.eyJ1aWQiOiAiMWQ3MDkxZjktMjk5ZS00ZGZjLTkzZDgtYmQ0ZWUxMWU1MTM5IiwgImlzcyI6ICJmaXJlYmFzZS1hZG1pbnNkay1vcndnb0Bmb3JkLW1vZGVsaW5nLmlhbS5nc2VydmljZWFjY291bnQuY29tIiwgImV4cCI6IDE1Nzk1OTk1NzksICJpYXQiOiAxNTc5NTk1OTc5LCAiYXVkIjogImh0dHBzOi8vaWRlbnRpdHl0b29sa2l0Lmdvb2dsZWFwaXMuY29tL2dvb2dsZS5pZGVudGl0eS5pZGVudGl0eXRvb2xraXQudjEuSWRlbnRpdHlUb29sa2l0IiwgInN1YiI6ICJmaXJlYmFzZS1hZG1pbnNkay1vcndnb0Bmb3JkLW1vZGVsaW5nLmlhbS5nc2VydmljZWFjY291bnQuY29tIn0.F_ZygUX9lVmUdWHk8Z81tDiwGSoSJhBC01asOdrp9qVxJRtaStE4-sGDStlNHUFclTS6bxPVUno26YnW8QfCJyES9Zm0S928IdUIeVpA_WgZi8bQoSgEJuCgYJN4WCmR09YPVF9C5mT8i4BCvMgYobDh_6OlHRNYi9OvNyDTL_dGVvEOGvQ_dIIIft80ILiFECxBpIxrMaXWHrtRwi4XoGqzCulvrrPT4Tag4MdbnBwW-AZZ0DtALDCIjAw24HMUPWyt_WcQfbOFsR-km-rwJSGFwTkObNeAXBtIwGvIMSjQfCH_pK7pOzLQ2PhCOAyCG6w1tjMQmG3cRKpMRFIakA", "firebase_token_expires": "2020-01-21T09:39:39.000000Z"}}
