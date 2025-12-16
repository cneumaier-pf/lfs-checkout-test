"""Tests for the hello.py script and LFS checkout verification."""

import subprocess
import sys
import os


def test_hello_output():
    """Test that hello.py prints 'hello world'."""
    result = subprocess.run(
        [sys.executable, "hello.py"],
        capture_output=True,
        text=True,
        cwd=os.path.dirname(os.path.abspath(__file__))
    )
    assert result.returncode == 0, f"hello.py failed with exit code {result.returncode}"
    assert result.stdout.strip() == "hello world", f"Expected 'hello world', got '{result.stdout.strip()}'"


def test_lfs_file_exists():
    """Test that the LFS file exists and is not just a pointer."""
    lfs_file = os.path.join(os.path.dirname(__file__), "testdata", "blob.bin")
    assert os.path.exists(lfs_file), f"LFS file {lfs_file} does not exist"
    
    # Check file size - LFS pointer files are typically very small (< 200 bytes)
    # A real binary file should be larger
    file_size = os.path.getsize(lfs_file)
    assert file_size > 200, f"LFS file appears to be a pointer (size: {file_size} bytes), not checked out"


def test_lfs_file_content():
    """Test that the LFS file has been properly checked out by verifying it's binary data."""
    lfs_file = os.path.join(os.path.dirname(__file__), "testdata", "blob.bin")
    
    with open(lfs_file, 'rb') as f:
        content = f.read(50)  # Read first 50 bytes
    
    # LFS pointer files start with "version https://git-lfs.github.com"
    # A properly checked out binary should NOT contain this text
    assert b"version https://git-lfs.github.com" not in content, \
        "LFS file appears to be a pointer file, not the actual binary content"
