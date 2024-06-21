import requests

class Doctors:
    def __init__(self, base_url, login_url, email, password):
        self.base_url = base_url
        self.login_url = login_url
        self.email = email
        self.password = password
        self.token = self.get_token()

    def get_token(self):
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "username": self.email,
            "password": self.password
        }
        response = requests.post(self.login_url, headers=headers, json=data)

        if response.status_code == 200:
            return response.json().get("token")
        else:
            raise Exception("Failed to authenticate")

    def get_doctors(self, params=None):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(self.base_url, headers=headers, params=params)

        import pdb; pdb.set_trace()
        if response.status_code == 200:
            return response.json()
        else:
            return None