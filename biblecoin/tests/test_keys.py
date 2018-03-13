import os
import biblecoin.tools.testutils as testutils
import biblecoin.utils as utils
from biblecoin.slogging import get_logger
import biblecoin.tools.keys as keys
logger = get_logger()


def test_key(filename, testname, testdata,):
    logger.debug('running test:%r in %r' % (testname, filename))
    assert keys.check_keystore_json(testdata["json"])
    privkey = keys.decode_keystore_json(testdata["json"], testdata["password"])
    assert utils.encode_hex(privkey) == testdata["priv"]


def pytest_generate_tests(metafunc):
    testutils.generate_test_params('KeyStoreTests', metafunc)
