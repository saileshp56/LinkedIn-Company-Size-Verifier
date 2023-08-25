# LinkedIn-Company-Size-Verifier
A program made with Selenium and Python for Public Services and Procurement Canada to verify the size of vendors. <br />
Step 1: Copy + paste the VNDR_LGL_NM column from your excel file into excel_column.txt <br /><br />
Step 2: Run excel_column_to_string_list.py <br /><br />
```
python3 excel_column_to_string_list.py
```
Step 3: Run main.py<br /><br />
```
python3 main.py
```
<br /><br />
When you run this and the program logs in, you may need to complete a captcha to prove you are not a robot.
<br /><br />
Be mindful of the fact that if you want to stop the program and run it again later, find the index of the last ran link, and put that index + 1 instead of 0 at line 40.<br /><br />
```python3 find_index.py```
