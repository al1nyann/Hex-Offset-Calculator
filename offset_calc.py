import argparse

def hex_to_int(hex_str):
    try:
        return int(hex_str, 16)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{hex_str}' is not a valid hexadecimal number.")

def main():
    parser = argparse.ArgumentParser(
        description="Calculate the offset (difference) between two hexadecimal addresses."
    )
    parser.add_argument("addr1", type=hex_to_int, help="First hex address (e.g. 55b4f6a09400)")
    parser.add_argument("addr2", type=hex_to_int, help="Second hex address (e.g. 55b4f6a0936a)")
    parser.add_argument("--reverse", action="store_true", help="Reverse subtraction (addr2 - addr1)")

    args = parser.parse_args()

    a = args.addr1
    b = args.addr2

    offset = b - a if args.reverse else a - b

    print(f"Address 1: {hex(a)}")
    print(f"Address 2: {hex(b)}")
    print(f"Offset: {offset} (dec) / {hex(offset)} (hex)")

if __name__ == "__main__":
    main()
