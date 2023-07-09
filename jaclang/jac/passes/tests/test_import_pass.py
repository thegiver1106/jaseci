"""Test pass module."""
from jaclang.jac.passes import ImportPass
from jaclang.jac.transpiler import jac_file_to_pass
from jaclang.utils.test import TestCase


class ImportPassPassTests(TestCase):
    """Test pass module."""

    def setUp(self) -> None:
        """Set up test."""
        return super().setUp()

    def test_pygen_jac_cli(self) -> None:
        """Basic test for pass."""
        state = jac_file_to_pass("base.jac", self.fixture_abs_path(""), ImportPass)
        self.assertFalse(state.errors_had)
        self.assertIn("56", str(state.ir.to_dict()))
