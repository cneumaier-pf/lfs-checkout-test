# LFS Checkout Test Repository

This repository is used to test Git LFS (Large File Storage) checkout functionality.

## Contents

- `hello.py` - A simple Python script that prints "hello world"
- `testdata/blob.bin` - A binary file tracked by Git LFS
- `test_hello.py` - Test suite for verifying functionality

## Running Tests

### Prerequisites

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Execute Tests

Run all tests with pytest:

```bash
pytest test_hello.py -v
```

Or simply:

```bash
pytest
```

### What the Tests Verify

1. **test_hello_output**: Verifies that `hello.py` runs successfully and outputs "hello world"
2. **test_lfs_file_exists**: Checks that the LFS-tracked binary file exists and is not just a pointer
3. **test_lfs_file_content**: Validates that the LFS file has been properly checked out (not a pointer file)

## Git LFS Setup

The repository uses Git LFS for binary file tracking. The `.gitattributes` file specifies:

```
testdata/blob.bin filter=lfs diff=lfs merge=lfs -text
```

For GitHub Actions workflows, the `.github/workflows/copilot-setup-steps.yaml` provides optimized LFS checkout with caching.
