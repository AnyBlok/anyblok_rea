# -*- coding: utf-8 -*-
# This file is a part of the AnyBlok project
#
#    Copyright (C) 2017 Simon ANDRE <sandre@anybox.fr>
#    Copyright (C) 2017 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
import os
from setuptools import setup, find_packages
version = '0.0.1'

requires = [
    'anyblok',
]

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst'), 'r', encoding='utf-8') as readme:
    README = readme.read()

with open(
    os.path.join(here, 'doc', 'CHANGES.rst'), 'r', encoding='utf-8'
) as change:
    CHANGE = change.read()

with open(
    os.path.join(here, 'doc', 'FRONT.rst'), 'r', encoding='utf-8'
) as front:
    FRONT = front.read()

setup(
    name="anyblok_rea",
    version=version,
    author="Simon ANDRE",
    author_email="sandre@anybox.fr",
    description="REA for AnyBlok",
    license="MPL2",
    long_description=README + '\n' + FRONT + '\n' + CHANGE,
    url="http://rea.anyblok.org/%s" % version,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=requires,
    tests_require=requires + ['nose'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
    ],
    entry_points={
        'bloks': [
            'rea=anyblok_rea.bloks.rea:REABlok',
            'rea-commitment=anyblok_rea.bloks.rea_commitment:REACommitmentBlok',
        ],
        'test_bloks': [
            'rea_test_1=anyblok_rea.test_bloks.test_1:TestBlok1',
        ],
    },
    extras_require={},
)
