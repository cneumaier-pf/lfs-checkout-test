import unittest
import sys
from io import StringIO
import importlib
import hello


class TestHello(unittest.TestCase):
    """Test cases for hello.py"""
    
    def test_hello_prints_correctly(self):
        """Test that hello.py prints 'hello world'"""
        # Capture stdout
        captured_output = StringIO()
        original_stdout = sys.stdout
        
        try:
            sys.stdout = captured_output
            # Import and run hello (which executes the print statement)
            importlib.reload(hello)
        finally:
            # Restore stdout
            sys.stdout = original_stdout
        
        # Verify output
        self.assertEqual(captured_output.getvalue().strip(), "hello world")


if __name__ == '__main__':
    unittest.main()
