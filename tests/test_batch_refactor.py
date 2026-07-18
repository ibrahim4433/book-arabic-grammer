import os
import sys
from pathlib import Path

# Add Jules-workspace to sys.path
sys.path.insert(0, str(Path("Jules-workspace").resolve()))

from batch_refactor import batch_refactor


def test_batch_refactor_dry_run(tmp_path, monkeypatch):
    # Setup dummy pages directory
    pages_dir = tmp_path / "pages"
    pages_dir.mkdir()

    test_file = pages_dir / "test.html"
    test_file.write_text('<div class="old-class"></div>', encoding="utf-8")

    # Mock os.walk to use our tmp_path
    def mock_walk(top, topdown=True, onerror=None, followlinks=False):
        return [(str(pages_dir), [], ["test.html"])]

    monkeypatch.setattr(os, "walk", mock_walk)

    # Run dry run
    batch_refactor(r"old-class", "new-class", dry_run=True, file_type=".html")

    # Assert file was NOT changed
    assert test_file.read_text(encoding="utf-8") == '<div class="old-class"></div>'


def test_batch_refactor_execute(tmp_path, monkeypatch):
    pages_dir = tmp_path / "pages"
    pages_dir.mkdir()

    test_file = pages_dir / "test.html"
    test_file.write_text('<div class="old-class"></div>', encoding="utf-8")

    def mock_walk(top, topdown=True, onerror=None, followlinks=False):
        return [(str(pages_dir), [], ["test.html"])]

    monkeypatch.setattr(os, "walk", mock_walk)

    # Run active refactor
    batch_refactor(r"old-class", "new-class", dry_run=False, file_type=".html")

    # Assert file WAS changed
    assert test_file.read_text(encoding="utf-8") == '<div class="new-class"></div>'
