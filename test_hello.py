"""Tests for the hello.py script and LFS checkout verification."""

import subprocess
import sys
import os


# Module-level constants
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
LFS_FILE_PATH = os.path.join(REPO_DIR, "testdata", "blob.bin")


def test_hello_output():
    """Test that hello.py prints 'hello world'."""
    result = subprocess.run(
        [sys.executable, "hello.py"],
        capture_output=True,
        text=True,
        cwd=REPO_DIR
    )
    assert result.returncode == 0, f"hello.py failed with exit code {result.returncode}"
    assert result.stdout.strip() == "hello world", f"Expected 'hello world', got '{result.stdout.strip()}'"


def test_lfs_file_exists():
    """Test that the LFS file exists and is not just a pointer."""
    assert os.path.exists(LFS_FILE_PATH), f"LFS file {LFS_FILE_PATH} does not exist"
    
    # Check file size - LFS pointer files are typically very small (< 200 bytes)
    # A real binary file should be larger
    file_size = os.path.getsize(LFS_FILE_PATH)
    assert file_size > 200, f"LFS file appears to be a pointer (size: {file_size} bytes), not checked out"


def test_lfs_file_content():
    """Test that the LFS file has been properly checked out by verifying it's binary data."""
    with open(LFS_FILE_PATH, 'rb') as f:
        content = f.read(50)  # Read first 50 bytes
    
    # LFS pointer files start with "version https://git-lfs.github.com"
    # A properly checked out binary should NOT contain this text
    assert b"version https://git-lfs.github.com" not in content, \
        "LFS file appears to be a pointer file, not the actual binary content"
