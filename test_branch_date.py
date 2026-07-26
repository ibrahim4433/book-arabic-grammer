import subprocess
from datetime import datetime, timezone
import dateutil.parser

out = subprocess.check_output(["git", "for-each-ref", "--format=%(refname:short)|%(committerdate:iso8601)", "refs/remotes/origin/"], text=True)
for line in out.splitlines()[:5]:
    print(line)
