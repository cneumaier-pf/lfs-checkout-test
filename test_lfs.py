"""Test for Git LFS file checkout."""
import os


# Constants
LFS_FILE_PATH = "testdata/blob.bin"
MIN_FILE_SIZE_BYTES = 1000  # LFS pointer files are typically < 200 bytes


def test_lfs_file_exists():
    """Test that the LFS file exists."""
    assert os.path.exists(LFS_FILE_PATH), f"LFS file {LFS_FILE_PATH} does not exist"


def test_lfs_file_size():
    """Test that the LFS file is the correct size (not a pointer file)."""
    file_size = os.path.getsize(LFS_FILE_PATH)
    # LFS pointer files are typically < 200 bytes
    # Real file should be much larger (5MB in this case)
    assert file_size > MIN_FILE_SIZE_BYTES, f"LFS file appears to be a pointer file (size: {file_size} bytes)"
    print(f"LFS file size: {file_size / (1024*1024):.2f} MB")


def test_lfs_file_is_binary():
    """Test that the LFS file contains binary data, not text."""
    with open(LFS_FILE_PATH, "rb") as f:
        content = f.read(100)
    # LFS pointer files start with "version https://git-lfs.github.com"
    # Real binary files should not contain this text
    assert not content.startswith(b"version https://git-lfs"), "LFS file appears to be a pointer file"


if __name__ == "__main__":
    test_lfs_file_exists()
    print("✓ test_lfs_file_exists passed")
    
    test_lfs_file_size()
    print("✓ test_lfs_file_size passed")
    
    test_lfs_file_is_binary()
    print("✓ test_lfs_file_is_binary passed")
