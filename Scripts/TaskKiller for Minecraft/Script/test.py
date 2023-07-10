import subprocess

out = subprocess.check_output(["tasklist", "/FI", '"SESSIONNAME', "eq", 'Services"', "/FO", "CSV"])
print(out)