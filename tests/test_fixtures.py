import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class FixtureTests(unittest.TestCase):
    def test_synthetic_records_match_documented_envelope(self):
        path = ROOT / 'fixtures' / 'records.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        self.assertEqual(data['dataset'], 'challenge')
        self.assertIsInstance(data['records'], list)
        self.assertGreaterEqual(len(data['records']), 3)
        identifiers = [row['id'] for row in data['records']]
        self.assertEqual(len(identifiers), len(set(identifiers)))
        self.assertTrue(all(isinstance(row, dict) for row in data['records']))

    def test_task_demand_support_access_and_trial_changes_are_distinguishable(self):
        data = json.loads((ROOT / 'fixtures' / 'records.json').read_text(encoding='utf-8'))
        self.assertEqual({row['version'] for row in data['catalogs']['tasks']}, {'v1', 'v2'})
        kinds = {row['kind'] for row in data['records']}
        self.assertTrue({'attempt', 'support-request', 'teacher-observation', 'trial-plan'} <= kinds)
        self.assertTrue(any(row.get('status') == 'unavailable' for row in data['records']))

if __name__ == '__main__':
    unittest.main()
