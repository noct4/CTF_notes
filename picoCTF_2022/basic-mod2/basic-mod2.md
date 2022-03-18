# basic-mod2
## Points: 100
## Tags: cryptography

---
## Notes
- A message is given as a download, with the instructions that we have to decrypt it with the given scheme.
- Similar to mod1, but with different number, different index for the cipher and obviously different message
- **"Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore."**
---
## Method
- Similar to the mod1 challenge, I made a script to perform the functions to the given message and output the flag. The code is below.
---
## Code
```python
cipher = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_']

encrypted = "268 413 110 190 426 419 108 229 310 379 323 373 385 236 92 96 169 321 284 185 154 137 186".split(" ")

flag = ""
for number in encrypted:
    modinv = pow(int(number), -1, 41)
    flag+=cipher[modinv]

print("picoCTF{"+flag+"}")
```
---
## Flag
**picoCTF{1NV3R53LY_H4RD_C680BDC1}**
---