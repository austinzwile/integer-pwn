#!/usr/bin/env python3

import ctypes
import argparse

def generate_truncation_input(target, start_bits, target_bits, start_signed, target_signed):
    # Validate bit sizes
    if target_bits >= start_bits:
        raise ValueError("Target bit size must be smaller than the start bit size.")

    # Calculate the mask for the truncated bits
    mask = (1 << target_bits) - 1

    # If the target is signed, adjust the target value to be correctly represented
    if target_signed:
        max_target_value = (1 << (target_bits - 1)) - 1
        min_target_value = -(1 << (target_bits - 1))
        if target > max_target_value or target < min_target_value:
            raise ValueError(f"Target value {target} is out of range for a signed {target_bits}-bit integer.")
        if target < 0:
            target &= mask  # Convert to unsigned equivalent
    else:
        max_target_value = (1 << target_bits) - 1
        if target < 0 or target > max_target_value:
            raise ValueError(f"Target value {target} is out of range for an unsigned {target_bits}-bit integer.")

    # Generate the input value that will truncate to the target value
    input_value = target  # Start with the target value
    if start_signed:
        input_value |= ~mask  # Set the higher bits if signed
    else:
        input_value |= (1 << (start_bits - target_bits))  # Set the higher bits if unsigned

    # Ensure the input value fits within the start bit size
    max_start_value = (1 << start_bits) - 1
    input_value &= max_start_value

    return input_value

def main():
    # Set up argparse
    parser = argparse.ArgumentParser(description="Generate an input value that, when truncated, matches the target value.")
    parser.add_argument("-t", "--target", type=int, required=True, help="The target integer value to match after truncation.")
    parser.add_argument("-sb", "--start_bits", type=int, choices=[8, 16, 32, 64], required=True, help="The bit size of the input value before truncation.")
    parser.add_argument("-tb", "--target_bits", type=int, choices=[8, 16, 32], required=True, help="The bit size of the value after truncation.")
    parser.add_argument("--start_signed", action="store_true", help="Specify if the input value is signed (default is unsigned).")
    parser.add_argument("--target_signed", action="store_true", help="Specify if the target value is signed (default is unsigned).")

    # Parse the arguments
    args = parser.parse_args()

    # Generate the input value
    try:
        input_value = generate_truncation_input(
            args.target, args.start_bits, args.target_bits, args.start_signed, args.target_signed
        )
        print(f"Generated input value: {hex(input_value)}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
