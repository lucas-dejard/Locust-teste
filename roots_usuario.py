from locust import HttpUser, TaskSet, task
from faker import Faker

class UserRouteLoadTest(TaskSet):

    faker = Faker()
    def on_start(self):
        print("Startou")

    def on_stop(self):
        print("Parou")

    @task()
    def test_list_users(self):
        self.client.get("/usuarios", name="Listar usuarios")

    @task()
    def test_create_users(self):
        self.client.post("/usuarios",
            name="Criar usuarios",
            json={
            "nome": f"pagarme{self.faker.name()}",
            "email": f"pagarme_{self.faker.name.split(' ')[0]}@pagar.me",
            "password": "teste",
            "administrador": "false"
        })

class WebsiteUser(HttpUser):
    tasks = [
        UserRouteLoadTest
    ]