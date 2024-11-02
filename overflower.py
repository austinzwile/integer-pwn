#!/usr/bin/env python3

import ctypes
import argparse

def calculate_overflow_or_underflow(initial, target, bitsize, signed=True, attack="overflow"):
    # Determine the maximum and minimum values based on the bit size and signedness
    if signed:
        max_value = (1 << (bitsize - 1)) - 1
        min_value = -(1 << (bitsize - 1))
    else:
        max_value = (1 << bitsize) - 1
        min_value = 0

    # Use ctypes to wrap the initial value in the appropriate type
    ctype = {8: ctypes.c_int8, 16: ctypes.c_int16, 32: ctypes.c_int32, 64: ctypes.c_int64}.get(bitsize)
    if not ctype:
        raise ValueError("Invalid bitsize. Must be one of 8, 16, 32, or 64.")

    initial_value = ctype(initial).value
    target_value = ctype(target).value

    # Calculate the difference based on the attack type
    if attack == "overflow":
        difference = (target_value - initial_value) if target_value > initial_value else (max_value - initial_value + target_value - min_value + 1)
    elif attack == "underflow":
        difference = (target_value - initial_value) if target_value < initial_value else (min_value - initial_value + target_value - max_value - 1)
    else:
        raise ValueError("Invalid attack type. Use 'overflow' or 'underflow'.")

    return difference

def main():
    # Set up argparse
    parser = argparse.ArgumentParser(description="Calculate the result of integer overflow/underflow.")
    parser.add_argument("-i", "--initial", type=int, required=True, help="The initial integer value.")
    parser.add_argument("-t", "--target", type=int, required=True, help="The target integer value.")
    parser.add_argument("-b", "--bitsize", type=int, choices=[8, 16, 32, 64], required=True, help="The bit size of the integer (8, 16, 32, or 64).")
    parser.add_argument("-s", "--signed", action="store_true", help="Specify if the integer is signed (default is unsigned).")
    parser.add_argument("-a", "--attack", choices=["overflow", "underflow"], required=True, help="Specify 'overflow' or 'underflow' to reach the target value.")

    # Parse the arguments
    args = parser.parse_args()

    # Calculate the difference
    result = calculate_overflow_or_underflow(args.initial, args.target, args.bitsize, args.signed, args.attack)

    # Print the result
    print(f"To go from {args.initial} to {args.target} with {args.bitsize}-bit "
          f"{'signed' if args.signed else 'unsigned'} integers, using {args.attack}, you need to add/subtract: {result}")

if __name__ == "__main__":
    main()

