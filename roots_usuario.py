from locust import HttpUser, TaskSet, task


class UserRouteLoadTest(TaskSet):

    def on_start(self):
        print("Startou")

    def on_stop(self):
        print("Parou")

    @task()
    def test_list_users(self):
        self.client.get("/usuarios", name="Listar usuarios")

    @task()
    def test_create_users(self):
        self.client.post("/usuarios", name="Criar usuarios", json={
            "nome": "pagarme foo bar",
            "email": "pagarme_qa@pagar.me",
            "password": "teste",
            "administrador": "false"
        })

class WebsiteUser(HttpUser):
    tasks = [
        UserRouteLoadTest
    ]