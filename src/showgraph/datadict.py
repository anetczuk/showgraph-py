# Copyright (c) 2022, Arkadiusz Netczuk <dev.arnet@gmail.com>
# All rights reserved.
#
# This source code is licensed under the BSD 3-Clause license found in the
# LICENSE file in the root directory of this source tree.
#

import os
import logging
import copy


SCRIPT_DIR = os.path.dirname( os.path.abspath(__file__) )

_LOGGER = logging.getLogger(__name__)


##
class DataDict():

    def __init__( self, data_dict=None ):
        self.data = data_dict
        if self.data is None:
            self.data = {}

    def rawdict(self):
        return copy.deepcopy( self.data )

    def keys(self):
        return list( self.data.keys() )

    def value( self, *keys, default=None ):
        try:
            curr_data = self.data
            for arg in keys:
                curr_data = curr_data[ arg ]
            return curr_data
        except KeyError as exc:
            _LOGGER.warning( "unable to get key %s in %s", exc, keys )
            return default

    def get( self, key, value=None ):
        try:
            return self.data[ key ]
        except KeyError as exc:
            _LOGGER.warning( "unable to get key %s", exc )
            return value

    def getOptional( self, key, value=None ):
        try:
            return self.data[ key ]
        except KeyError:
            return value

    def setValue( self, key, item, *args ):
        """ Set dictionary value. 
            There are two mandatory values:
               'key'  -- dictionary key
               'item' -- other value
            Depending on optional arguments 'item' will be subkey or value to insert.
            For example: data.setValue( "key1", 123 ) will create "key1" with value 123.
            Call: data.setValue( "key1", "subkey2", 123 ) will create subdict containing value 123.
        """

        args_size = len( args )
        if args_size < 1:
            set_value( self.data, key, item )
            return
        if args_size == 1:
            curr_data = self.data.setdefault( key, {} )
            data_val  = args[0]
            set_value( curr_data, item, data_val )
            return

        curr_data = self.data.setdefault( key, {} )
        curr_data = curr_data.setdefault( item, {} )
        for i in range( 0, args_size - 2 ):
            subkey = args[i]
            curr_data = curr_data.setdefault( subkey, {} )
        last_key = args[-2]
        value    = args[-1]
        set_value( curr_data, last_key, value )

    def setSubdict( self, key, *args ):
        """ Set dictionary subdict with given keys list. """
        args_size = len( args )
        if args_size < 1:
            self.data.setdefault( key, {} )
            return
        curr_data = self.data.setdefault( key, {} )
        for subkey in args:
            curr_data = curr_data.setdefault( subkey, {} )


def set_value( data_dict, key, value):
    if key not in data_dict:
        ## no data -- add new entry
        data_dict[ key ] = value
        return
    curr_item = data_dict[ key ]
    if isinstance( curr_item, dict ):
        ## current data is dict -- override with value
        data_dict[ key ] = value
        return
    if isinstance( curr_item, list ):
        ## current data is list -- append
        data_dict[ key ].append( value )
        return
    ## regular type -- override
    data_dict[ key ] = [ data_dict[ key ], value ]


## ==================================================


def get_create_item( dict_obj, key, default_val ):
    if key not in dict_obj:
        dict_obj[ key ] = default_val
    return dict_obj[ key ]
