# vim: ai ts=4 sts=4 et sw=4
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
import sys
from jhvm.parser import parse_input
from jhvm.genast import generate_bytecode
from jhvm.vm import VirtualMachine
from rpython.rlib.streamio import open_file_as_stream
def usage():
    print 'Usage: target-vm compiled-bytecode'
    return 1

def entry_point(argv):
    if len(argv) < 1:
        usage()

    filename = argv[1]
    contents = open_file_as_stream(argv[1]).readall()
    ast = parse_input(contents)
    bytecode = generate_bytecode(ast)
    vm = VirtualMachine(bytecode)
    res = vm.interp()
    print res.value
    return 0

def target(*args):
    return entry_point

if __name__ == '__main__':
    entry_point(sys.argv)



