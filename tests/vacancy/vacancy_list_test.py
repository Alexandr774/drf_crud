import pytest

from user.models import User

@pytest.mark.django_db
def test_vacancy_list(client):
    vacancy = {
        "first_name":"user_test",
        "last_name":"0000",
        "username":"resr",
        "password":"qwe",
        "age": 21
}


    expected_response = {
    "id": 1,
    "location": None,
    "first_name": "user_test",
    "last_name": "0000",
    "username": "resr",
    "password": "qwe",
    "role": "",
    "age": 21
}

    response = client.post('/use/create/', vacancy, content_type='application/json')
    assert response.data == expected_response
    assert response.status_code == 201
#


# @pytest.mark.django_db
# def test_vacancy_list(client):
#
#     expected_response = {
#     "id": 1,
#     "location": "Москва, м. Студенческая",
#     "first_name": "Павел",
#     "last_name": "Никифоров",
#     "username": "pnikifirov",
#     "password": "gZvptL",
#     "role": "member",
#     "age": 21
# }
#
#     response = client.get("/use/1/")
#
#     assert response.data == expected_response
#     assert response.status_code == 404
#
