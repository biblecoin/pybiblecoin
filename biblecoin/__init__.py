# -*- coding: utf-8 -*-
# ############# version ##################
try:
    from pkg_resources import get_distribution, DistributionNotFound
except BaseException:
    DistributionNotFound = Exception
import os.path
import subprocess
import re
# Import slogging to patch logging as soon as possible
from . import slogging  # noqa


GIT_DESCRIBE_RE = re.compile(
    '^(?P<version>v\d+\.\d+\.\d+)-(?P<git>\d+-g[a-fA-F0-9]+(?:-dirty)?)$')


__version__ = None
try:
    _dist = get_distribution('biblecoin')
    # Normalize case for Windows systems
    dist_loc = os.path.normcase(_dist.location)
    here = os.path.normcase(__file__)
    if not here.startswith(os.path.join(dist_loc, 'biblecoin')):
        # not installed, but there is another version that *is*
        raise DistributionNotFound
    __version__ = _dist.version
except DistributionNotFound:
    pass

if not __version__:
    try:
        rev = subprocess.check_output(['git', 'describe', '--tags', '--dirty'],
                                      stderr=subprocess.STDOUT)
        match = GIT_DESCRIBE_RE.match(rev)
        if match:
            __version__ = "{}+git-{}".format(
                match.group("version"), match.group("git"))
    except BaseException:  # FIXME!
        pass

if not __version__:
    __version__ = 'undefined'

# ########### endversion ##################

"""from biblecoin import utils
from biblecoin import trie
from biblecoin import securetrie
from biblecoin import blocks
from biblecoin import transactions
from biblecoin import processblock
from biblecoin import tester
from biblecoin import abi
from biblecoin import keys
from biblecoin import ethash"""
