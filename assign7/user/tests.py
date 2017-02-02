from django.test import TestCase, Client
from django.contrib.auth.models import User, AnonymousUser
from django.core.urlresolvers import reverse
from django.db import DatabaseError
from mock import patch

# Create your tests here.
class HealthTestCase(TestCase):
    def setUp(self):
        self.c = Client()
        self.status_fields = ['db', 'status']

    def test_health_endpoint_ok(self):
        url = reverse('health-list')
        response = self.c.get(url)
        assert response.status_code == 200, \
            "Expect 200 OK. got: {}" . format (response.status_code)

        expected_fields = ["db", "status"]

        for field in self.status_fields:
            assert response.json().get("status", {}).get(field, None) == "up", \
                "Expected field {} to exist" . format (field)

    @patch.object(User.objects, 'first')
    def test_determine_db_status(self, mock_query):
        """Health should not be ok if it cannot connect to the db"""

        mock_query.side_effect = DatabaseError()
        url = reverse('health-list')
        response = self.c.get(url)

        status = response.json().get("status", {})
        db_status = status.get('db')
        assert db_status == 'down', \
            'Expect DB to be down. Got: {}' . format (db_status)

        status = status.get('status')
        assert status == 'down', \
            'Expect status to be down. Got: {}' . format (status)

class UserAPITestCase(TestCase):

    """
    User API
    """

    def setUp(self):
        self.c = Client()

        self.normal_user = User.objects.create_user(
            username="joe", password="password", email="joe@soap.com")
        self.superuser = User.objects.create_superuser(
            username="clark", password="supersecret", email="joe@soap.com")

    def test_can_get_user_list(self):
        """GET /user returns a list of users"""
        url = reverse("user-list")
        response = self.c.get(url)

        assert response.status_code == 200, \
            "Expect 200 OK. got: {}" . format(response.status_code)
        num_users = len(response.json())

        assert num_users == 2, \
            "Expect it to return exactly 2 users. Got: {}" . format(num_users)

    def test_get_user_returns_correct_fields(self):
            """GET /user/{pk} returns a user"""

            expected_fields = ['url', 'username', 'email', 'is_staff']
            url = reverse("user-detail", args=[self.normal_user.pk])
            response = self.c.get(url)

            assert response.status_code == 200, \
                "Expect 200 OK. got: {}" . format(response.status_code)

            assert response.json()["is_staff"] == False
            assert response.json()["username"] == "joe"
            assert response.json()["email"] == "joe@soap.com"
            expected_url = "http://testserver/users/{}/" . format(
                self.normal_user.pk)
            assert response.json()["url"] == expected_url, \
                'Expect url to be set. Got: {}' . format(response.json()["url"])

    def tearDown(self):
        for user in User.objects.all():
            user.delete()
