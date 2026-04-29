import importlib
import os
import sys
from unittest import TestCase
from unittest.mock import patch


class SettingsModuleTests(TestCase):
    def _reload_settings(self):
        # Force module re-evaluation so each test gets isolated env/argv behavior.
        if "config.settings" in sys.modules:
            return importlib.reload(sys.modules["config.settings"])
        return importlib.import_module("config.settings")

    def test_uses_in_memory_sqlite_when_test_command_is_run(self):
        # Arrange
        env = {
            "POSTGRES_HOST": "",
            "AZURE_POSTGRES_HOST": "",
            "DJANGO_DEBUG": "false",
        }
        argv = ["manage.py", "test"]

        # Act
        with patch.dict(os.environ, env, clear=False), patch.object(sys, "argv", argv):
            settings = self._reload_settings()

        # Assert
        self.assertEqual(settings.DATABASES["default"]["ENGINE"], "django.db.backends.sqlite3")
        self.assertEqual(settings.DATABASES["default"]["NAME"], ":memory:")

    def test_uses_azure_defaults_when_only_azure_host_is_provided(self):
        # Arrange
        env = {
            "POSTGRES_HOST": "",
            "AZURE_POSTGRES_HOST": "dicle-backend-db.postgres.database.azure.com",
            "POSTGRES_DB": "",
            "POSTGRES_USER": "",
            "AZURE_POSTGRES_USER": "",
            "POSTGRES_PASSWORD": "",
            "POSTGRES_PORT": "",
            "AZURE_POSTGRES_PORT": "",
            "POSTGRES_CONN_MAX_AGE": "",
            "POSTGRES_SSLMODE": "",
        }
        argv = ["manage.py", "runserver"]

        # Act
        with patch.dict(os.environ, env, clear=False), patch.object(sys, "argv", argv):
            settings = self._reload_settings()

        # Assert
        default_db = settings.DATABASES["default"]
        self.assertEqual(default_db["ENGINE"], "django.db.backends.postgresql")
        self.assertEqual(default_db["NAME"], "postgres")
        self.assertEqual(default_db["USER"], "db_manager")
        self.assertEqual(default_db["PASSWORD"], "")
        self.assertEqual(default_db["HOST"], "dicle-backend-db.postgres.database.azure.com")
        self.assertEqual(default_db["PORT"], "5432")
        self.assertEqual(default_db["CONN_MAX_AGE"], 60)
        self.assertEqual(default_db["OPTIONS"]["sslmode"], "require")

    def test_prefers_explicit_postgres_environment_values(self):
        # Arrange
        env = {
            "POSTGRES_HOST": "custom-postgres-host",
            "AZURE_POSTGRES_HOST": "ignored-azure-host",
            "POSTGRES_DB": "app_db",
            "POSTGRES_USER": "app_user",
            "POSTGRES_PASSWORD": "app_password",
            "POSTGRES_PORT": "6432",
            "POSTGRES_CONN_MAX_AGE": "120",
            "POSTGRES_SSLMODE": "verify-full",
        }
        argv = ["manage.py", "runserver"]

        # Act
        with patch.dict(os.environ, env, clear=False), patch.object(sys, "argv", argv):
            settings = self._reload_settings()

        # Assert
        default_db = settings.DATABASES["default"]
        self.assertEqual(default_db["NAME"], "app_db")
        self.assertEqual(default_db["USER"], "app_user")
        self.assertEqual(default_db["PASSWORD"], "app_password")
        self.assertEqual(default_db["HOST"], "custom-postgres-host")
        self.assertEqual(default_db["PORT"], "6432")
        self.assertEqual(default_db["CONN_MAX_AGE"], 120)
        self.assertEqual(default_db["OPTIONS"]["sslmode"], "verify-full")

    def test_falls_back_to_file_sqlite_when_postgres_hosts_are_empty(self):
        # Arrange
        env = {
            "POSTGRES_HOST": "",
            "AZURE_POSTGRES_HOST": "",
        }
        argv = ["manage.py", "migrate"]

        # Act
        with patch.dict(os.environ, env, clear=False), patch.object(sys, "argv", argv):
            settings = self._reload_settings()

        # Assert
        default_db = settings.DATABASES["default"]
        self.assertEqual(default_db["ENGINE"], "django.db.backends.sqlite3")
        self.assertEqual(str(default_db["NAME"]), str(settings.BASE_DIR / "db.sqlite3"))

    def test_parses_allowed_hosts_and_cors_origins_with_empty_values(self):
        # Arrange
        env = {
            "DJANGO_ALLOWED_HOSTS": " localhost, ,127.0.0.1,,api.local ",
            "CORS_ALLOWED_ORIGINS": " http://localhost:3000, ,https://frontend.local ,, ",
        }
        argv = ["manage.py", "runserver"]

        # Act
        with patch.dict(os.environ, env, clear=False), patch.object(sys, "argv", argv):
            settings = self._reload_settings()

        # Assert
        self.assertEqual(settings.ALLOWED_HOSTS, ["localhost", "127.0.0.1", "api.local"])
        self.assertEqual(
            settings.CORS_ALLOWED_ORIGINS,
            ["http://localhost:3000", "https://frontend.local"],
        )

    def test_debug_and_jwt_lifetimes_are_parsed_from_environment(self):
        # Arrange
        env = {
            "DJANGO_DEBUG": "yes",
            "JWT_ACCESS_MINUTES": "15",
            "JWT_REFRESH_DAYS": "14",
        }
        argv = ["manage.py", "runserver"]

        # Act
        with patch.dict(os.environ, env, clear=False), patch.object(sys, "argv", argv):
            settings = self._reload_settings()

        # Assert
        self.assertTrue(settings.DEBUG)
        self.assertEqual(settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].total_seconds(), 900)
        self.assertEqual(settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"].days, 14)
