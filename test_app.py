#!/usr/bin/env python3
"""
Tests unitarios para app.py
"""

import unittest
from unittest.mock import patch, MagicMock
import sys
import io
import datetime
import platform

# Importar las funciones desde app.py
sys.path.insert(0, ".")
from app import proceso_simple


class TestProcesoSimple(unittest.TestCase):
    """Tests para la función proceso_simple"""

    @patch("app.time.sleep")
    @patch("app.random.randint")
    def test_proceso_simple_numeros_altos(self, mock_randint, mock_sleep):
        """Test que verifica detección de números altos"""
        mock_randint.return_value = 85
        mock_sleep.side_effect = KeyboardInterrupt()

        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            proceso_simple()
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Aplicación Python iniciada", output)
        self.assertIn("Iteración #1", output)
        self.assertIn("85", output)
        self.assertIn("Número alto detectado", output)

    @patch("app.time.sleep")
    @patch("app.random.randint")
    def test_proceso_simple_numeros_bajos(self, mock_randint, mock_sleep):
        """Test que verifica detección de números bajos"""
        mock_randint.return_value = 15
        mock_sleep.side_effect = KeyboardInterrupt()

        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            proceso_simple()
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Número bajo detectado", output)
        self.assertIn("15", output)

    @patch("app.time.sleep")
    @patch("app.random.randint")
    def test_proceso_simple_numeros_medios(self, mock_randint, mock_sleep):
        """Test que verifica números en rango medio"""
        mock_randint.return_value = 50
        mock_sleep.side_effect = KeyboardInterrupt()

        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            proceso_simple()
        except SystemExit:
            pass

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Iteración #1", output)
        self.assertIn("50", output)
        self.assertNotIn("Número alto detectado", output)
        self.assertNotIn("Número bajo detectado", output)

    def test_imports(self):
        """Test que verifica que los módulos se importan correctamente"""
        import time
        import datetime
        import platform
        import random

        self.assertIsNotNone(time)
        self.assertIsNotNone(datetime)
        self.assertIsNotNone(platform)
        self.assertIsNotNone(random)

    def test_platform_info(self):
        """Test que verifica información del sistema"""
        sistema = platform.system()
        version = platform.python_version()

        self.assertIsInstance(sistema, str)
        self.assertIsInstance(version, str)
        self.assertTrue(len(sistema) > 0)
        self.assertTrue(len(version) > 0)


if __name__ == "__main__":
    unittest.main()
