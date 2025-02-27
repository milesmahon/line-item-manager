#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import os.path

def get_txt(filename):
    with open(filename) as txt_file:
        return txt_file.read()

readme = get_txt('README.rst') if os.path.isfile('README.rst') else ''
history = get_txt('HISTORY.rst') if os.path.isfile('HISTORY.rst') else ''

requirements = [
    'backports-datetime-fromisoformat==1.0.0',
    'Click==7.1.2',
    'googleads==25.0.0',
    'jinja2==2.11.3',
    'jsonschema==3.2.0',
    'PyYAML>=5.4',
    'retrying==1.3.3',
    'tqdm==4.56.0',
]

package_data = [
    'conf.d/*.yml',
    'conf.d/*.yaml',
]

release_requirements = [
    'bump2version>=1',
    'twine==3.2.0',
]

setup_requirements = []

test_requirements = [
    'coverage==5.3',
    'flake8==3.8.4',
    'mock==4.0.2',
    'pytest==6.1.2',
    'pytest-cov==2.10.1',
    'pytest-runner==5.3.0',
 ]

setup(
    author="the prebid contributors",
    author_email='info@prebid.org',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="Create and manage line items.",
    entry_points={
        'console_scripts': [
            'line_item_manager=line_item_manager.cli:main',
        ],
    },
    extras_require={
        'release': release_requirements,
        'test': test_requirements,
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='line-item-manager',
    name='line-item-manager',
    packages=find_packages(include=['line_item_manager', 'line_item_manager.*']),
    package_dir={'line_item_manager': 'line_item_manager'},
    package_data={'line_item_manager': package_data},
    setup_requires=setup_requirements,
    test_suite='tests',
    url='https://github.com/prebid/line-item-manager',
    version='0.2.4',
    zip_safe=False,
)
