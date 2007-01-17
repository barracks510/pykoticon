#! /usr/bin/env python
# -*- coding: ISO-8859-15 -*-

# PyKotIcon - Client side helper for PyKota and other applications
#
# (c) 2003, 2004, 2005, 2006, 2007 Jerome Alet <alet@librelogiciel.com>
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

"""This test program demonstrates the functionnalities of PyKotIcon.

Launch pykoticon with no arguments on the same host, then launch
this test program this way :

        $ python ./test.py localhost 7654

Then you should see the demonstration begin.

Please send bug reports or feedback to : alet@librelogiciel.com"""

import sys
import socket
import xmlrpclib


def main(arguments) :
    """Main function."""
    # Opens the connection to the PyKotIcon server :
    server = xmlrpclib.ServerProxy("http://%s:%s" % (arguments[0], arguments[1]))
    
    # Now display something on the PyKotIcon host :
    message1 = "You are about to test PyKotIcon\n\nPyKotIcon is really great software !"
    server.showDialog(xmlrpclib.Binary(message1.encode("UTF-8")), False)
    
    # Now ask the end user if he really wants to do this : 
    message2 = "Are you sure you want to do this ?"
    result = server.showDialog(xmlrpclib.Binary(message2.encode("UTF-8")), True)
    print "The remote user said : %s" % result
    
    # Displays the answer back :
    answer = "You have clicked on the %s button" % result
    server.showDialog(xmlrpclib.Binary(answer.encode("UTF-8")), False)
    
    # Now we will ask some datas : 
    result = server.askDatas([xmlrpclib.Binary(v) for v in ["Username", "Password", "Country"]], \
                             ["username", "password", "country"], \
                             {"username": xmlrpclib.Binary(""), \
                              "password": xmlrpclib.Binary(""), \
                              "country" : xmlrpclib.Binary("")})
    if result["isValid"] :
        print "Answers :"
        print "\n".join(["\t%s => '%s'" % (k, v.data) for (k, v) in result.items() if k != "isValid"])
        answer = "You answered :\n%s" % "\n".join(["%s => '%s'" % (k, v.data) for (k, v) in result.items() if k != "isValid"])
        server.showDialog(xmlrpclib.Binary(answer.encode("UTF-8")), False)
    else :    
        print "The answers are not valid."
        
    # Now do nothing :    
    server.nop()
        
    # Finally we will cause PyKotIcon to die
    message3 = "As soon as you'll click on the button below, PyKotIcon will die."
    server.showDialog(xmlrpclib.Binary(message3.encode("UTF-8")), False)
    server.quitApplication()
    
    # That's all folks !
    print
    print "This demo is finished. Did you like it ?"
        
if __name__ == "__main__" :
    if len(sys.argv) < 3 :
        sys.stderr.write("usage : %s pykoticon_hostname_or_ip_address pykoticon_TCPPort\n" % sys.argv[0])
    else :    
        try :
            main(sys.argv[1:])
        except socket.error, msg :    
            sys.stderr.write("ERROR : Network error : %s\n" % msg)
            sys.stderr.write("Are you sure that PyKotIcon is running and accepts incoming connections ?\n")
            
