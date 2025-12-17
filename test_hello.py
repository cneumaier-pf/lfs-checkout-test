"""Test for hello.py script."""
import subprocess
import sys


def test_hello_output():
    """Test that hello.py prints 'hello world'."""
    result = subprocess.run(
        [sys.executable, "hello.py"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"Script failed with return code {result.returncode}"
    assert result.stdout.strip() == "hello world", f"Expected 'hello world', got '{result.stdout.strip()}'"


if __name__ == "__main__":
    test_hello_output()
    print("✓ test_hello_output passed")
