"""Tests de submódulo de catálogos."""

import pytest

from etl.catalog.catalog import StatesCodes

NUM_STATES = 33  # Uno mas por el asignado al país completo
VALID_STATES = ["AGUASCALIENTES", "BAJA_CALIFORNIA", "CAMPECHE", "YUCATAN"]


class TestStateCode:
    """Test catálogo de códigos de estados mexicanos."""

    def test_valid_number_of_states(self) -> None:
        """Revisa que el número de estados en el Enum sea igual al esperado."""
        assert len(StatesCodes) == NUM_STATES

    @pytest.mark.parametrize("state", VALID_STATES)
    def test_expected_members(self, state: str) -> None:
        """Revisa que contenga todos los estados esperados el catálogo."""
        assert state in StatesCodes._member_names_
