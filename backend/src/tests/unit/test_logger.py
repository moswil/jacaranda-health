import io

from app.utils.logger import get_logger


def test_normal_logger():
    out = io.StringIO()
    LOGGER = get_logger()
    test_string = 'Hello World'
    LOGGER.info(test_string)
    output = out.getvalue().strip()
    if test_string in output:
        assert True
    else:
        assert not False
