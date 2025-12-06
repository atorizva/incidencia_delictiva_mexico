"""Cliente para conexión con API de INEGI."""

import os

import requests
from dotenv import load_dotenv

# Dict que relaciona datos de la API con su código
API_DATA_CODES: dict[str, int] = {
    "public_space_robbery_or_assault_crime_rate_data": 6200028409
}


class ApiClient:
    """Cliente de conexión a API de INEGI.

    Contiene distintos métodos para extracción de datos.
    """

    def __init__(self) -> None:
        self._session = requests.Session()  # Misma sesión para las peticiones
        self._base_url = "https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR"
        self.token: str = self._get_token()

    def _get_token(self) -> str:
        """Obtiene el token para utilizar la API de INEGI del entorno."""
        if token := os.getenv("API_TOKEN"):
            return token
        raise ValueError("API_TOKEN no encontrada.")  # noqa: TRY003

    def _build_url(self, indicator_code: int) -> str:
        """Construye una url válida para de la API de INEGI."""
        return (
            f"{self._base_url}/{indicator_code}"
            + f"/es/0/false/BISE/2.0/{self.token}?type=json"
        )

    def get_data(self, data_code: int) -> requests.Response:
        """Obtiene datos de acuerdo con el código de datos asociado.

        Realiza una petición `get` a la API de INEGI para obtener datos asociados
        con un código específico.

        Args:
            data_code (int): código asociado a una base de datos específica en la
            API de INEGI.
        """
        return self._session.get(self._build_url(data_code))


if __name__ == "__main__":
    from pprint import pprint

    # Cargar token de la API
    load_dotenv()

    # Petición
    api = ApiClient()
    response = api.get_data(
        API_DATA_CODES["public_space_robbery_or_assault_crime_rate_data"]
    )
    pprint(response.json())
