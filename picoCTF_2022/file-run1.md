# file-run1
## Points: 100
## Tags: Reverse Engineering

---
## Notes
- Downloading and looking at the program, there is not much we can get from it. It needs to be given execute permissions to run before we can execute.
- After trying to execute, it appears that the binary doesn't run (wasn'rt sure this this was just on my end, I am on an M1 machine but also tried it on an Intel-based Mac and had the same issue)
- Was able to find the flag using the strings command
---
## Method
- Running the command ```strings run``` gave an output of all the strings in the binary, including the flag
---
## Flag
**picoCTF{U51N6_Y0Ur_F1r57_F113_9bc52b6b}**
---