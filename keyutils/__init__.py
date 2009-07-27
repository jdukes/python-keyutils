#!/usr/bin/python
#
# Copyright (c) 2009 rPath, Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#

import _keyutils
for k, v in _keyutils.__dict__.items():
    if k.startswith('E'):
        globals()[k] = v
del k, v

def add_key(key, value, keyring, keyType = "user"):
    return _keyutils.add_key(keyType, key, value, keyring)

def request_key(key, keyring, keyType = "user"):
    return _keyutils.request_key(keyType, key, keyring)

def read_key(keyId):
    return _keyutils.read_key(keyId)