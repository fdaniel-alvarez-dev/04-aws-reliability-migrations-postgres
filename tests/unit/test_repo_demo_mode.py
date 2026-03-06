from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


class TestRepoDemoMode(unittest.TestCase):
    def test_problem_statement_present(self) -> None:
        content = (REPO_ROOT / "04-problem-statement.txt").read_text(encoding="utf-8")
        self.assertIn("Top 3 pain points", content)

    def test_migrations_present(self) -> None:
        migrations = sorted((REPO_ROOT / "migrations").glob("*.up.sql"))
        self.assertGreaterEqual(len(migrations), 3)

    def test_migration_scripts_present(self) -> None:
        for script in ("migrate.sh", "migrate_status.sh", "migrate_rollback.sh"):
            self.assertTrue((REPO_ROOT / "scripts" / script).exists())

    def test_readme_mentions_migrations_targets(self) -> None:
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("zero/low-downtime migrations", readme.lower())

    def test_notice_present(self) -> None:
        notice = (REPO_ROOT / "NOTICE.md").read_text(encoding="utf-8")
        self.assertIn("CloudForgeLabs", notice)
        self.assertIn("Freddy D. Alvarez", notice)

