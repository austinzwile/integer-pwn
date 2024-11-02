>  _       _
(_)_ __ | |_ ___  __ _  ___ _ __      _ ____      ___ __
| | '_ \| __/ _ \/ _` |/ _ \ '__|____| '_ \ \ /\ / / '_ \
| | | | | ||  __/ (_| |  __/ | |_____| |_) \ V  V /| | | |
|_|_| |_|\__\___|\__, |\___|_|       | .__/ \_/\_/ |_| |_|
                 |___/               |_|

---
This tool was designed with the sole purpose of helping you calculate two types of vulnerabilities.

 1. Integer Overflows/Underflow Vulnerabilities
 2. Integer Truncation Vulnerabilities

The repo comes with two tools named appropriately to help you calculate the values needed in order to properly exploit an integer-related vulnerability given a certain set of circumstances.

Both tools work in a similar way.

In the overflow tool, you provide a starting value, a target value, bitsize and whether you you want to overflow or underflow to reach the target value and then it will generate the proper value for you to provide to your program to reach that input.

In the truncation tool, you provide a target value, a starting bitsize and a target bitsize, and then it will generate a value that, when provided to the program, will equal the target value post-truncation.

Enjoy!!
