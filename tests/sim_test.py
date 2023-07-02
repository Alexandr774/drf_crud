import pytest


@pytest.mark.django_db
def test_1(client):
    response = client.get('/use/')
    assert response.status_code == 200