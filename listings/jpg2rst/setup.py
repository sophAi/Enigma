#!/usr/bin/env python
# =======================================================================
# File Name     : setup.py
# Creation Time : 20130708 10:15:21
# Last Modified : 20130712 23:33:04
# =======================================================================
# Copyright (c),2012-, Po-Jen Hsu. Contact: clusterga@gmail.com
# This software is distributed under the GNU General Public License.
# See the README file in the top-level directory.
# =======================================================================
from setuptools import setup, find_packages
setup(
    name = 'jpg2rst',
    version = '0.1',
    author = 'Po-Jen Hsu',
    author_email = 'clusterga@gmail.com',
    description = 'Tools for Restructured Text Documentation',
    license='GPL',
    py_modules = ['jpg2rst', 'fig_tools', 'file_tools', 'rst_tools'],
    zip_safe = False,
#    packages = find_packages(),
   )
