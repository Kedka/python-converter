import sys
import runpy
from decoder import binary_to_text, hex_to_text, octal_to_text

test_string = "the quick brown fox jumps over the lazy dog"


def test_binary_to_text():
    binary_string = [format(ord(char), "b") for char in test_string]
    result = binary_to_text(binary_string)

    assert "".join(result) == test_string


def test_hex_to_text():
    hex_string = [hex(ord(char)) for char in test_string]
    result = hex_to_text(hex_string)

    assert result == test_string


def test_octal_to_text():
    octal_string = [oct(ord(char)) for char in test_string]
    result = octal_to_text(octal_string)

    assert "".join(result) == test_string


def test_system(capsys):
    # Test binary, input -> "a b c"
    sys.argv[1:] = ["bin", "01100001", "00100000", "01100010", "00100000", "01100011"]
    runpy.run_module("decoder", run_name="__main__")

    # Test hexadecimal, input -> "a b c"
    sys.argv[1:] = ["hex", "61", "20", "62", "20", "63"]
    runpy.run_module("decoder", run_name="__main__")

    # Test octal, input -> "a b c"
    sys.argv[1:] = ["oct", "141", "40", "142", "40", "143"]
    runpy.run_module("decoder", run_name="__main__")

    captured = capsys.readouterr()
    message_stack = captured.out.rstrip().split("\n")

    # Assert from the last message to the first
    assert message_stack.pop() == "a b c"
    assert message_stack.pop() == "['141', '40', '142', '40', '143']"
    assert message_stack.pop() == "a b c"
    assert message_stack.pop() == "['61', '20', '62', '20', '63']"
    assert message_stack.pop() == "a b c"
    assert (
        message_stack.pop()
        == "['01100001', '00100000', '01100010', '00100000', '01100011']"
    )
    assert not message_stack
