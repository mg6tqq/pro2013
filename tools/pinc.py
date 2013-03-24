import sys
import re
import shlex
import subprocess as sp

exe_pat = re.compile(r'(\s*)\(!>(.*)<\)\s*')
inc_pat = re.compile(r'(\s*)\(>(.*)<\)\s*')

if __name__ == "__main__":
  for line in sys.stdin:
    match_exe = re.match(exe_pat, line)
    match_inc = re.match(inc_pat, line)
    if match_exe:
      space = match_exe.group(1)
      exe = match_exe.group(2).strip()
      args = shlex.split(exe)
      sys.stdout.writelines(map(lambda x: space+x+"\n", sp.check_output(args).split("\n")))
    elif match_inc:
      space = match_inc.group(1)
      inc = match_inc.group(2).strip()
      sys.stdout.writelines(map(lambda x: space+x, open(inc)))
    else:
      sys.stdout.write(line)
