import subprocess
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
validator = ROOT / "scripts" / "validate_site.rb"

result = subprocess.run(["ruby", str(validator)], cwd=ROOT)
sys.exit(result.returncode)
