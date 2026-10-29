import unittest
from unittest.mock import patch

from app import get_db_config


class TestApp(unittest.TestCase):

    @patch.dict(
        "os.environ",
        {
            "DB_HOST": "postgres-db",
            "DB_PORT": "5432",
            "DB_NAME": "myapp",
            "DB_USER": "postgres",
        },
    )
    def test_get_db_config(self):
        config = get_db_config("mysecret")

        self.assertEqual(config["host"], "postgres-db")
        self.assertEqual(config["port"], 5432)
        self.assertEqual(config["dbname"], "myapp")
        self.assertEqual(config["user"], "postgres")
        self.assertEqual(config["password"], "mysecret")


if __name__ == "__main__":
    unittest.main()
