# Copyright (c) 2022, Arkadiusz Netczuk <dev.arnet@gmail.com>
# All rights reserved.
#
# This source code is licensed under the BSD 3-Clause license found in the
# LICENSE file in the root directory of this source tree.
#

import unittest

from showgraph.datadict import DataDict


class DataDictTest(unittest.TestCase):
    def setUp(self):
        ## Called before testfunction is executed
        pass

    def tearDown(self):
        ## Called after testfunction was executed
        pass

    def test_get(self):
        data = DataDict()
        value = data.get( 'aaa', 'bbb' )
        self.assertEqual( value, "bbb" )

    def test_get_default(self):
        data = DataDict()
        value = data.get( 'aaa', value='xxx' )
        self.assertEqual( value, "xxx" )

    def test_value(self):
        data = DataDict()
        value = data.value( 'aaa', 'bbb' )
        self.assertEqual( value, None )

    def test_value_default(self):
        data = DataDict()
        value = data.value( 'aaa', 'bbb', default='xxx' )
        self.assertEqual( value, "xxx" )

    def test_setValue_0(self):
        data = DataDict()
        data.setValue( "key1", 123 )
        self.assertEqual( {'key1': 123}, data.rawdict() )

    def test_setValue_1(self):
        data = DataDict()
        data.setValue( "key1", "key2", 123 )
        self.assertEqual( {'key1': {'key2': 123}}, data.rawdict() )

    def test_setValue_2(self):
        data = DataDict()
        data.setValue( "key1", "key2", "key3", 123 )
        self.assertEqual( {'key1': {'key2': {'key3': 123}}}, data.rawdict() )

    def test_setValue_3(self):
        data = DataDict()
        data.setValue( "key1", "key2", "key3", "key4", 123 )
        self.assertEqual( {'key1': {'key2': {'key3': {'key4': 123}}}}, data.rawdict() )

    def test_setValue_many(self):
        data = DataDict()
        data.setValue( "1", "2b", "3c", "4a" )
        data.setValue( "1", "2b", "3d" )

        self.assertEqual( {'1': {'2b': '3d'}}, data.rawdict() )

    def test_setSubdict_0(self):
        data = DataDict()
        data.setSubdict( "key1", 123 )
        self.assertEqual( {'key1': {123: {}}}, data.rawdict() )

    def test_setSubdict_1(self):
        data = DataDict()
        data.setSubdict( "key1", "key2", 123 )
        self.assertEqual( {'key1': {'key2': {123: {}}}}, data.rawdict() )

    def test_setSubdict_2(self):
        data = DataDict()
        data.setSubdict( "key1", "key2", "key3", 123 )
        self.assertEqual( {'key1': {'key2': {'key3': {123: {}}}}}, data.rawdict() )

    def test_setSubdict_3(self):
        data = DataDict()
        data.setSubdict( "key1", "key2", "key3", "key4", 123 )
        self.assertEqual( {'key1': {'key2': {'key3': {'key4': {123: {}}}}}}, data.rawdict() )

    def test_setSubdict_many(self):
        data = DataDict()
        data.setSubdict( "1", "2b", "3c", "4a" )
        data.setSubdict( "1", "2b", "3d" )

        self.assertEqual( {'1': {'2b': {'3c': {'4a': {}}, '3d': {}}}}, data.rawdict() )
