from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

# requirements
install_requires = list(x.strip() for x in open('requirements.txt'))
install_requires_replacements = {
    'https://github.com/ethereum/ethash/tarball/master': 'pyethash',
}
install_requires = [
    install_requires_replacements.get(
        r, r) for r in install_requires]

# dev requirements
tests_require = list(x.strip() for x in open('dev_requirements.txt'))

# dependency links
dependency_links = []

# *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
# see:
# https://github.com/biblecoin/pyethapp/wiki/Development:-Versions-and-Releases
version = '2.3.0'

setup(
    name="biblecoin",
    packages=find_packages("."),
    description='Next generation cryptocurrency network',
    long_description=readme,
    url='https://github.com/biblecoin/pybiblecoin/',
    install_requires=install_requires,
    tests_require=tests_require,
    dependency_links=dependency_links,
    setup_requires=[
        #    'pytest-runner==2.7'
    ],
    version=version,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
