from setuptools import setup

from setup_utils.utils import VersionFinder, LongDescriptionFinder

version = VersionFinder().find_version()

long_desc = ''
with LongDescriptionFinder() as ld:
    long_desc = ld.get_desc_from_readme()

setup(
    name='ml-flow',
    version=version[1:-1],
    description='An Iterative Applied Machine Learning Framework',
    long_description=long_desc,
    url='https://github.com/Saransh-git/ml-flow.git',
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
