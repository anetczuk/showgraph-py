#!/usr/bin/env python3
#
# Copyright (c) 2022, Arkadiusz Netczuk <dev.arnet@gmail.com>
# All rights reserved.
#
# This source code is licensed under the BSD 3-Clause license found in the
# LICENSE file in the root directory of this source tree.
#

import sys
import os

import logging
import unittest
import re
import argparse


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

src_dir = os.path.abspath( os.path.join(SCRIPT_DIR, os.pardir, os.pardir, "src") )
sys.path.insert(0, src_dir)


from showgraph.datadict import DataDict
from showgraph.graphviz import Graph


_LOGGER = logging.getLogger(__name__)



## ============================= main section ===================================


def generate():
    data_tree = DataDict()
    data_tree.setSubdict( "a", "b", "d" )
    data_tree.setSubdict( "a", "b", "e" )
    data_tree.setSubdict( "a", "c", "f", "h" )
    data_tree.setSubdict( "a", "c", "g" )
    graph_data = data_tree.rawdict()

    graph = Graph()
    generate_graph( graph, graph_data )

    graph_path = os.path.join( SCRIPT_DIR, "graph.png" )
    graph.writePNG( graph_path )

    graph_path = os.path.join( SCRIPT_DIR, "graph.gv.txt" )
    graph.writeRAW( graph_path )


def generate_graph( graph: Graph, data, parent_node=None ):
    if isinstance( data, dict ):
        for key, val in data.items():
            generate_graph( graph, key, parent_node )
            generate_graph( graph, val, key )
        return
    if isinstance( data, list ):
        for val in data:
            generate_graph( graph, val, parent_node )
        return
    ## value -- add node and edge
    graph.addNode( data )
    if parent_node:
        graph.addEdge( parent_node, data )


if __name__ == '__main__':
    generate()
