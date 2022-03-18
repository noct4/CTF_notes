# Forbidden Paths
## Points: 200
## Tags: Web Exploitation

---
## Notes
- We are told in the brief that the website files live in ```/usr/share/nginx/html/``` and the flag is within ```/flag.txt```
- Since we can't use absolute paths, we must use relative paths to access ```/flag.txt```
- This means we need to start at the directory where the web page is hosted and traverse back to the directory where ```flag.txt``` is located
---
## Method
- Providing the path ```../../../../flag.txt``` to the input box and clicking read will access the file and give us the flag
---
## Flag
**picoCTF{7h3_p47h_70_5ucc355_6db46514}**
---