import pytest
from greetlab.cli import main
import sys
def test_blank_name_raise_exit():
    # 传入仅空白字符的name，预期触发SystemExit，返回码为2
    with pytest.raises(SystemExit) as exc_info:
        sys.argv = ["cli.py", "--name", "   "]
        main()
    assert exc_info.value.code == 2
