#! /usr/bin/env python
# -*- coding: ISO-8859-15 -*-

# PyKotIcon - an end-user companion for PyKota
#
# (c) 2003-2004 Jerome Alet <alet@librelogiciel.com>
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
#
# $Id$
#
#

from distutils.core import setup
import sys
import os
import glob
try :
    import py2exe
except ImportError :
    if sys.platform == "win32" :
        sys.stderr.write("py2exe is not installed ! ABORTING.\n")
        sys.exit(-1)
    else :    
        withPy2EXE = 0
else :        
    withPy2EXE = 1

version = "0.1"

setup(name = "pykoticon", version = version,
      license = "GNU GPL",
      description = "an end-user companion for PyKota",
      author = "Jerome Alet",
      author_email = "alet@librelogiciel.com",
      url = "http://www.librelogiciel.com/software/",
      windows=[os.path.join("bin", "pykoticon")],
      scripts=[os.path.join("bin", "pykoticon")],
      data_files=[("icons", glob.glob(os.path.join("icons", "*.ico")))])
