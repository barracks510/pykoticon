#! /usr/bin/env python
# -*- coding: ISO-8859-15 -*-

# PyKotIcon - an end-user companion for PyKota
#
# (c) 2003, 2004, 2005, 2006 Jerome Alet <alet@librelogiciel.com>
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

import sys
import os
import time
import xmlrpclib

def main(arguments) :
    """Main function."""
    printername = os.environ.get("PYKOTAPRINTERNAME")
    username = os.environ.get("PYKOTAUSERNAME")
    jobid = os.environ.get("PYKOTAJOBID")
    jobtitle = os.environ.get("PYKOTATITLE")
    jobsize = os.environ.get("PYKOTAPRECOMPUTEDJOBSIZE")
    try :
        server = xmlrpclib.ServerProxy("http://%s:%s" % (arguments[0], arguments[1]))
        result = server.openConfirmDialog(printername, username, jobid, jobtitle, jobsize)
    except :    
        sys.stderr.write("An error occured !\n")
    if result != "OK" :
        print result
        
if __name__ == "__main__" :
    if len(sys.argv) != 3 :
        sys.stderr.write("usage : %s printing_client_hostname_or_ip_address printing_client_TCPPort\n" % sys.argv[0])
    else :    
        main(sys.argv[1:])
