#!/usr/bin/env python3
"""Simple test runner for the repository."""
import sys
import traceback


def run_tests():
    """Run all tests."""
    tests_passed = 0
    tests_failed = 0
    
    test_modules = [
        ("test_hello", ["test_hello_output"]),
        ("test_lfs", ["test_lfs_file_exists", "test_lfs_file_size", "test_lfs_file_is_binary"])
    ]
    
    print("=" * 60)
    print("Running tests...")
    print("=" * 60)
    
    for module_name, test_functions in test_modules:
        print(f"\n{module_name}.py:")
        try:
            module = __import__(module_name)
            for test_name in test_functions:
                try:
                    test_func = getattr(module, test_name)
                    test_func()
                    print(f"  ✓ {test_name}")
                    tests_passed += 1
                except AssertionError as e:
                    print(f"  ✗ {test_name}: {e}")
                    tests_failed += 1
                except Exception as e:
                    print(f"  ✗ {test_name}: {type(e).__name__}: {e}")
                    traceback.print_exc()
                    tests_failed += 1
        except ImportError as e:
            print(f"  ✗ Failed to import {module_name}: {e}")
            tests_failed += len(test_functions)
    
    print("\n" + "=" * 60)
    print(f"Results: {tests_passed} passed, {tests_failed} failed")
    print("=" * 60)
    
    return 0 if tests_failed == 0 else 1


if __name__ == "__main__":
    sys.exit(run_tests())
