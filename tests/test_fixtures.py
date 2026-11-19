import csv
import unittest
from pathlib import Path


class FixtureTests(unittest.TestCase):
    def test_slots_data_has_multiple_record_types_and_targets(self):
        path = Path(__file__).parents[1] / "fixtures" / "slots.csv"
        with path.open(encoding="utf-8", newline="") as source:
            rows = list(csv.DictReader(source))
        self.assertTrue({"eligibility", "application", "slot", "contact"} <= {r["record_type"] for r in rows})
        self.assertGreaterEqual(len({row["goal_id"] for row in rows}), 4)


if __name__ == "__main__":
    unittest.main()
