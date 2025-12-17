"""Test for Git LFS file checkout."""
import os


def test_lfs_file_exists():
    """Test that the LFS file exists."""
    lfs_file = "testdata/blob.bin"
    assert os.path.exists(lfs_file), f"LFS file {lfs_file} does not exist"


def test_lfs_file_size():
    """Test that the LFS file is the correct size (not a pointer file)."""
    lfs_file = "testdata/blob.bin"
    file_size = os.path.getsize(lfs_file)
    # LFS pointer files are typically < 200 bytes
    # Real file should be much larger (5MB in this case)
    assert file_size > 1000, f"LFS file appears to be a pointer file (size: {file_size} bytes)"
    print(f"LFS file size: {file_size / (1024*1024):.2f} MB")


def test_lfs_file_is_binary():
    """Test that the LFS file contains binary data, not text."""
    lfs_file = "testdata/blob.bin"
    with open(lfs_file, "rb") as f:
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
