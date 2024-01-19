import sys
from typing import Iterable


def binary_to_text_generator(input: list) -> Iterable[str]:
    for char in input:
        bits = int(char, 2)
        yield bits.to_bytes((bits.bit_length() + 7) // 8, "big").decode()


def binary_to_text(input: list[str]) -> str:
    return to_string(binary_to_text_generator(input))


def hex_to_text(input: list[str]) -> str:
    text = " ".join(sanitize_input(input))
    return bytes.fromhex(text).decode("utf-8")


def octal_to_text(input: list[str]) -> str:
    text = sanitize_input(input)
    return to_string([chr(int(char, 8)) for char in text])


def sanitize_input(input: list[str]) -> list[str]:
    return [word.replace("0x", "").replace("0o", "") for word in input]


def to_string(input: list[str] | Iterable[str]) -> str:
    return "".join(input)


def help():
    print(
        "----------------------------------------------------\n"
        "Translates binary, hexadecimal or octal code to text\n"
        "----------------------------------------------------\n"
        "Usage:\n"
        "  bin BIN_VALUES\n"
        "      Accepts a list of values separated with spaces\n"
        "  hex HEX_VALUES\n"
        "      Accepts a list of values separated with spaces\n"
        "  oct OCT_VALUES\n"
        "      Accepts a list of values separated with spaces\n"
        "  exit\n"
        "      Exits program\n"
        "----------------------------------------------------\n"
    )
    sys.exit(2)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        help()

    cmd = sys.argv[1]
    value = sys.argv[2:]
    print(value)

    match cmd:
        case "bin":
            print(binary_to_text(value))
        case "hex":
            print(hex_to_text(value))
        case "oct":
            print(octal_to_text(value))
        case "exit":
            sys.exit(0)
        case _:
            help()
