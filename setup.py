from setuptools import setup
import re


class VersionException(Exception):
    def __init__(self):
        super().__init__('Version not defined')


version = None
for line in open('./ml_flow/__init__.py'):  # decoupling modules from setup, instead of importing here
    match = re.fullmatch(r"__version__ *= *('.*')", line)

    if match:
        version, = match.groups()
        break

if not version:
    raise VersionException

setup(
    name='ml-flow',
    version=version[1:-1],
    description='An Iterative Applied Machine Learning Framework',
    url='saranshk.com',  # TODO: replace it with GitHub uri
    author='Saransh Kumar',
    author_email='kumar.saransh@gmail.com',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Machine Learning Engineering',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires="~=3.8.2",
    install_requires=[
        'ipython',
        'jupyter',
        'qtconsole',
        'pandas',
        'numpy',
        'scipy',
        'sklearn',
        'matplotlib'
    ]

)
