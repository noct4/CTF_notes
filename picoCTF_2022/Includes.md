# Includes
## Points: 100
## Tags: web exploitation, inspector

---
## Notes
- The description of the problem and the hint on the page told us to look for code that is not initially in the inspector
- This web page had the associated CSS and JS file which each contained half of the flag
---
## Method
- Open up the inspector to see the code for the web page
- The first half of the flag is contained within the CSS file, accessed by going to the 'style editor' tab in the inspector
- The second half of the password is contained within 'script.js', which can be found inside the sources section of the 'debugger' tab. Selecting the file will show the js code that is contained within it that the button on the page calls. 
---
## Flag
**picoCTF{1nclu51v17y_1of2_f7w_2of2_df589022}**
---