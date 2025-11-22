"""Cliente para conexión con API de INEGI."""

import os

import requests
from dotenv import load_dotenv


class ApiClient:
    """Cliente de conexión a API de INEGI.

    Contiene distintos métodos para extracción de datos.
    """

    def __init__(self) -> None:
        self._session = requests.Session()  # Misma sesión para las peticiones
        self._base_url = "https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR"
        self.token: str = self._get_token()

    def _get_token(self) -> str:
        if token := os.getenv("API_TOKEN"):
            return token
        raise ValueError("API_TOKEN no encontrada.")  # noqa: TRY003

    def _build_url(self, indicator_code: int) -> str:
        return (
            f"{self._base_url}/{indicator_code}"
            + f"/es/0/false/BISE/2.0/{self.token}?type=json"
        )

    def get_public_space_robbery_or_assault_crime_rate(
        self,
    ) -> requests.Response:
        """
        Obtiene la tasa de robos o asaltos en via pública por cada 100k habitantes.
        """
        code = 6200028409
        return self._session.get(self._build_url(code))


if __name__ == "__main__":
    from pprint import pprint

    # Cargar token de la API
    load_dotenv()

    # Petición
    api = ApiClient()
    response = api.get_public_space_robbery_or_assault_crime_rate()
    pprint(response.json())
