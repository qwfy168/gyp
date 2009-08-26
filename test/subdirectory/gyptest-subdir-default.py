#!/usr/bin/env python

"""
Verifies building a subsidiary dependent target from a .gyp file in a
subdirectory, without specifying an explicit output build directory,
and using the subdirectory's solution or project file as the entry point.
"""

import TestGyp

test = TestGyp.TestGyp()

test.run_gyp('prog1.gyp')

test.build_default('prog2.gyp', chdir='subdir')

test.must_not_exist('prog1'+test._exe)

test.run_built_executable('prog2',
                          chdir='subdir',
                          stdout="Hello from prog2.c\n")

test.pass_test()