"""Pruebas unitarias para conexión con API."""

import os
from unittest.mock import MagicMock, Mock

import pytest

from etl.extraction.api_client import ApiClient

TEST_TOKEN = "ABC123"


@pytest.fixture
def set_api_token(mocker: MagicMock) -> None:
    """Define API_TOKEN como variable de entorno."""
    mocker.patch.dict(os.environ, {"API_TOKEN": TEST_TOKEN})


@pytest.fixture
def api_client(set_api_token: None) -> ApiClient:  # noqa: ARG001
    """Inicializa un ApiClient correctamente."""
    return ApiClient()


class TestApiClient:
    """Tests para la clase ApiClient."""

    def test_client_token(self, api_client: ApiClient) -> None:
        """Valida el contenido de API_TOKEN."""
        assert api_client.token == TEST_TOKEN

    def test_incorrect_client_init(self) -> None:
        """Valida que no se pueda inicializar el cliente sin API_TOKEN."""
        os.environ.pop("API_TOKEN")
        with pytest.raises(ValueError, match=r"API_TOKEN no encontrada."):
            ApiClient()

    @pytest.mark.parametrize("code", [1, 10, 500, 999])
    def test_build_url(self, api_client: ApiClient, code: int) -> None:
        """Valida que la construcción de la url sea correcta."""
        expected_url = (
            f"{api_client._base_url}/{code}/es/0/false/BISE/2.0/{TEST_TOKEN}?type=json"
        )
        assert api_client._build_url(code) == expected_url

    @pytest.mark.parametrize("code", [1, 10, 500, 999])
    def test_request(self, mocker: MagicMock, api_client: ApiClient, code: int) -> None:
        """Valida que se ejecute una petición GET."""
        mock_response = Mock()

        mock_get = mocker.patch.object(
            api_client, "get_data", return_value=mock_response
        )

        api_client.get_data(code)

        mock_get.assert_called_once()
