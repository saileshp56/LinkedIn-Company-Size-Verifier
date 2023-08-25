# Open the input file
# you should copy paste the VNDR_LGL_NM excel column in here
with open('sample_excel_column.txt', 'r') as file:
    lines = file.readlines()


formatted_lines = set()  # use a set to remove duplicates
for line in lines:
    # format the line
    line = line.strip()
    # Add quotes around the line to make it a string
    formatted_line = '"' + line + '",'
    # Add the formatted line to the set
    formatted_lines.add(formatted_line)


# Write the unique formatted lines to a new file
with open('excel_column_strings.txt', 'w') as file:
    file.write("[")
    file.writelines(formatted_lines)
    file.write("]")

