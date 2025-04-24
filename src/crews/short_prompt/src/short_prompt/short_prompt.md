Convert the input_text from decimal to hexadecimal and binary.

For non_negative_integer input, if it's 0, output '0' in hexadecimal and binary. Otherwise, append the remainder to hexadecimal and '0' or '1' to binary based on the boolean result of dividing by 16 and 2 respectively, until the input becomes 0.

Example:
Input: 12 (non_negative_integer)
Expected Output:
- Hexadecimal: 0 C 
- Binary: 1100

Input: 1024 (non_negative_integer)
Expected Output:
- Hexadecimal: 400 0 0 0 0 0 0 0 
- Binary: 10000000000