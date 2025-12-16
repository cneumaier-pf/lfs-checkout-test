import subprocess
import sys


def test_hello_world_output():
    """Test that hello.py prints 'hello world'."""
    result = subprocess.run(
        [sys.executable, "hello.py"],
        capture_output=True,
        text=True,
        check=True
    )
    assert result.stdout.strip() == "hello world"
    assert result.returncode == 0
