import json
import tempfile
import unittest
from pathlib import Path


class ConfigurationLoadTest(unittest.TestCase):
    def test_configuration_round_trip(self):
        sample_config = {
            "hourOn1_1": "08",
            "minOn1_1": "00",
            "hourOff1_1": "20",
            "minOff1_1": "00",
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "config.json"
            with config_path.open("w", encoding="utf-8") as config_file:
                json.dump(sample_config, config_file)

            with config_path.open(encoding="utf-8") as loaded_file:
                loaded_config = json.load(loaded_file)

        self.assertEqual(loaded_config["hourOn1_1"], sample_config["hourOn1_1"])
        self.assertEqual(loaded_config["minOn1_1"], sample_config["minOn1_1"])
        self.assertEqual(loaded_config["hourOff1_1"], sample_config["hourOff1_1"])
        self.assertEqual(loaded_config["minOff1_1"], sample_config["minOff1_1"])


if __name__ == "__main__":
    unittest.main()
