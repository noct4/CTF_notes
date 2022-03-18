## Solution to basic-mod1 problem in picoCTF2022

cipher = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_']

encrypted = "54 396 131 198 225 258 87 258 128 211 57 235 114 258 144 220 39 175 330 338 297 288".split(" ")

flag = ""
for number in encrypted:
    mod = int(number) % 37
    flag+=cipher[mod]

print("picoCTF{"+flag+"}")