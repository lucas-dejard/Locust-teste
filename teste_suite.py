from locust import HttpUser
from roots_usuario import UserRouteLoadTest


class WebSiteUser(HttpUser):
    tasks = [
        UserRouteLoadTest
    ]