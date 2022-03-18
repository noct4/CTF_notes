## Solution to basic-mod2 problem in picoCTF2022

cipher = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_']

encrypted = "268 413 110 190 426 419 108 229 310 379 323 373 385 236 92 96 169 321 284 185 154 137 186".split(" ")

flag = ""
for number in encrypted:
    modinv = pow(int(number), -1, 41)
    flag+=cipher[modinv]

print("picoCTF{"+flag+"}")