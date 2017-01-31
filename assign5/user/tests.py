from django.test import TestCase, Client
from django.contrib.auth.models import User, AnonymousUser
from django.core.urlresolvers import reverse

# Create your tests here.
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
