# Enhance!
## Points: 100
## Tags: Forensics, svg

---
## Notes
- We are given an SVG to analyse, as well as no hints.
- Since an SVG is a vector image, we can open it up in a text editor and see the makeup of the file.
- In this challenge, the flag is split up among different lines, and so was not easily identifiable when using a tool such as strings via CMD. 
---
## Method
- Opening the SVG in an editor showed the code of the file, and analysing that the flag is visible in lines 85-120. The flag is split up on the lines and so must be put back together.
---
## Flag
**picoCTF{3nh4nc3d_aab729dd}**
---