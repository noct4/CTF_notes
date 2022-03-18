# Power Cookie
## Points: 200
## Tags: web exploitation, cookie

---
## Notes
- The only thing initially interesting on the page is the button labelled 'Continue as guest'
- Clicking the button during recon, we can see a page showing 'We apologize, but we have no guest services at the moment.'
- Opening up a cookie inspector, we see an isAdmin cookie, set with the value of 0. This likely controls the admin privileges to the site and thus by changing it we can get admin access and the flag.
---
## Method
- Click on the button labelled with 'Continue as guest'
- When shown the guest access page, open up the cookie editor and change the **idAdmin** cookie value from a 0 to a 1
- Refresh the page and the flag is shown, indicating admin privileges.
---
## Flag
**picoCTF{gr4d3_A_c00k13_5d2505be}**
---