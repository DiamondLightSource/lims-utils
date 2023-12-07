import subprocess
import sys

from expeye_utils import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "expeye_utils", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
