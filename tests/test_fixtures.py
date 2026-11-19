import csv
from pathlib import Path
import unittest


FIXTURES = Path(__file__).resolve().parents[1] / "fixtures"
HEADERS = {'plans': ['id', 'trial', 'batch', 'claimed_g', 'status'], 'adjustments': ['id', 'measurement', 'new_g', 'recorded'], 'policy': ['min_pairs', 'abs_max_waste', 'min_original', 'min_fulfilled'], 'batches': ['id', 'day', 'service', 'grams'], 'trials': ['id', 'batch', 'window', 'floor', 'arm', 'day'], 'demand': ['id', 'trial', 'arrival', 'wanted', 'served', 'requested_size', 'served_size', 'fulfilled'], 'refills': ['demand', 'grams'], 'weighings': ['id', 'kind', 'applies_to', 'grams'], 'diversions': ['demand', 'source_trial', 'dest_trial', 'minute']}
LINKS = [('trials', 'batch', 'batches', 'id'), ('demand', 'trial', 'trials', 'id'), ('refills', 'demand', 'demand', 'id'), ('plans', 'batch', 'batches', 'id'), ('adjustments', 'measurement', 'weighings', 'id')]


def read(name):
    with (FIXTURES / (name + ".csv")).open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        return reader.fieldnames, list(reader)


class SourceRecords(unittest.TestCase):
    def test_records_match_source_columns(self):
        for name, expected in HEADERS.items():
            with self.subTest(table=name):
                header, rows = read(name)
                self.assertEqual(header, expected)
                self.assertTrue(rows)
                self.assertTrue(all(None not in row and None not in row.values() for row in rows))
                if "id" in header:
                    ids = [row["id"] for row in rows]
                    self.assertTrue(all(ids))
                    self.assertEqual(len(ids), len(set(ids)))

    def test_record_references_exist(self):
        for source, field, target, key in LINKS:
            with self.subTest(table=source, column=field):
                _, source_rows = read(source)
                _, target_rows = read(target)
                keys = {row[key] for row in target_rows}
                self.assertTrue(all(row[field] in keys for row in source_rows))
