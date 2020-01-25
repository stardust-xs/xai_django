# Copyright 2020 XAMES3. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ======================================================================
"""Learning Django's implementation."""

from setuptools import find_packages, setup


def use_readme() -> str:
  """Use `README.md` for parsing long description."""
  with open('README.md') as file:
    return file.read()


with open('requirements.txt', 'r') as requirements:
  required_packages = [package.rstrip() for package in requirements]

setup(
  name='mle_django',
  version='0.1 (beta)',
  author='XA',
  classifiers=[
    'Development Status :: 1 - Planning',
    'Development Status :: 2 - Pre-Alpha',
    'Framework :: Django :: 3.0',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'License :: OSI Approved :: PostgreSQL License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Database',
    'Topic :: Internet :: WWW/HTTP :: WSGI',
    ],
  description=__doc__,
  long_description=use_readme(),
  long_description_content_type='text/markdown',
  keywords='mle django webapplication',
  zip_safe=False,
  install_requires=required_packages,
  python_requires='~=3.6',
  include_package_data=True,
  packages=find_packages(),
)
