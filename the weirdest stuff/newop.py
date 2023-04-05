import re

# Define the set_variable function as before
def set_variable(variable_name, regex_expression):
    regex = re.compile(regex_expression)
    valid_chars = set(regex.findall("".join(chr(i) for i in range(128))))
    globals()[variable_name] = list(valid_chars)

# Read in the script file
with open("script.txt") as f:
    script_lines = f.readlines()

# Loop over each line in the script file
for i, line in enumerate(script_lines):
    # Check if the line contains a variable assignment with a regex expression
    match = re.match(r"([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.+)", line)
    if match:
        variable_name = match.group(1)
        regex_expression = match.group(2)

        # Convert the line to a call to set_variable
        new_line = f"set_variable('{variable_name}', r'{regex_expression}')\n"

        # Replace the original line with the new line
        script_lines[i] = new_line

# Write the modified script back out to a file
with open("modified_script.py", "w") as f:
    f.write("from newop import set_variable\n")
    f.writelines(script_lines)

exec(open("modified_script.py").read())
