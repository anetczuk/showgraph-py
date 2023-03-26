#!/usr/bin/env python3

import os

from setuptools import setup, find_packages

from showgraph.io import read_list


SCRIPT_DIR = os.path.dirname( os.path.abspath(__file__) )


packages_list = find_packages( include=['showgraph', 'showgraph.*'] )

data_files = [ ( "showgraph", ["graphviz_dark_colors.data.txt"] ) ]

requirements_path = os.path.join( SCRIPT_DIR, "requirements.txt" )
install_reqs  = read_list( requirements_path )

## every time setup info changes then version number should be increased

setup( name='showgraph',
       version='2.0.2',
       description='draw data relations in form of graph structure',
       url='https://github.com/anetczuk/showgraph-py',
       author="anetczuk",
       license="BSD 3-Clause License",
       packages=packages_list,
       data_files=data_files,
       install_requires=install_reqs
       )
