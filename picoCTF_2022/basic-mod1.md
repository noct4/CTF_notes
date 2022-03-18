# basic-mod1
## Points: 100
## Tags: cryptography

---
## Notes
- A message is given as a download, with the instructions that we have to decrypt it with the given scheme
- **"Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore"**
---
## Method
- I made a quick python script to go through all the numbers, mod37 them and then assign them the relevant value from the cipher. The code is below.
---
## Code
```python
cipher = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_']

encrypted = "54 396 131 198 225 258 87 258 128 211 57 235 114 258 144 220 39 175 330 338 297 288".split(" ")

flag = ""
for number in encrypted:
    mod = int(number) % 37
    flag+=cipher[mod]

print("picoCTF{"+flag+"}")
```
---
## Flag
**picoCTF{R0UND_N_R0UND_79C18FB3}**
---