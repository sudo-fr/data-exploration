""" this is the test file for the module1 of package1 """
from package1.module1 import print_hello


def test_print_hello(capfd):
    """Test the print_hello function"""
    # Call the function
    print_hello()

    # Capture the output
    captured = capfd.readouterr()

    # Check if the output is correct
    assert captured.out == "Hello from module1\n"
