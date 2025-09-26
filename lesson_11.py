import requests

class LegalAPI:
    """
    Класс для работы с Legal API (https://legal-api.sirotinsky.com/).
    Обеспечивает взаимодействие с методами API ЕФРСБ.
    """

    BASE_URL = "https://legal-api.sirotinsky.com"

    def __init__(self, token: str):
        """
        Инициализация экземпляра API клиента.

        :param token: токен для авторизации
        """
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json"
        }

    def _get(self, endpoint: str, params: dict = None):
        """
        Внутренний метод для выполнения GET-запроса.
        """
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()  # выбросит ошибку при неудаче
        return response.json()

    def _post(self, endpoint: str, data: dict = None):
        """
        Внутренний метод для выполнения POST-запроса.
        """
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()
