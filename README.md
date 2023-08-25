# LinkedIn-Company-Size-Verifier
A program made with Selenium and Python for Public Services and Procurement Canada to verify the size of vendors. <br />
Step 1: Copy + paste the VNDR_LGL_NM column from your excel file into excel_column.txt <br /><br />
Step 2: Run excel_column_to_string_list.py <br /><br />
```
python3 excel_column_to_string_list.py
```
Step 3: Set the output of paste excel_column_strings.txt into links_list by copy + pasting the contents of the text file<br /><br />
Step 4: Run main.py<br /><br />
```
python3 main.py
```
<br /><br />
When you run this and the program logs in, you may need to complete a captcha to prove you are not a robot.
<br /><br />

Be mindful of the fact that if you want to stop the program and run it again later, run find_index.py, and put the returned value instead of 0 at line 40.<br /><br />

You'll need to put the output of paste excel_column_strings.txt into links_list by copy + pasting the contents of the text file
```
python3 find_index.py
```
<br />
ALSO: The program will reprint the headers of the excel file, so you'll want to delete that (but it should be fine if you leave it too)
<br /><br />

Next Steps: On a LinkedIn company profile, you could check for Affiliated Pages, and select the LinkedIn page classified as Parent 
