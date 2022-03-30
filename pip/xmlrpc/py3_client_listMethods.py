#!/usr/bin/env python3
import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
# Print list of available methods
print(s.system.listMethods())
