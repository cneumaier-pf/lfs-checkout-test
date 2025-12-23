# LFS Checkout Test Repository

This repository is designed to test Git LFS (Large File Storage) checkout functionality.

## Contents

- `hello.py` - A simple Python script that prints "hello world"
- `testdata/blob.bin` - A 5MB binary file tracked by Git LFS
- `test_hello.py` - Tests for the hello.py script
- `test_lfs.py` - Tests to verify LFS files are properly checked out
- `run_tests.py` - Test runner script

## Running Tests

To run all tests, simply execute:

```bash
python3 run_tests.py
```

Or run individual test files:

```bash
python3 test_hello.py
python3 test_lfs.py
```

## Test Coverage

The test suite verifies:

1. **hello.py functionality** - Ensures the script runs and produces correct output
2. **LFS file checkout** - Verifies that LFS files are properly downloaded (not just pointer files)
3. **Binary data integrity** - Confirms that LFS files contain actual binary data

## Requirements

- Python 3.x
- Git with LFS support (for proper file checkout)

## GitHub Actions

The repository includes a workflow (`.github/workflows/copilot-setup-steps.yaml`) that sets up the environment with proper LFS checkout using `nschloe/action-cached-lfs-checkout@v1.2.3`.
