#!/usr/bin/python
#==============================================================================
# archive_data.py
# Downloads data from the One Platform and outputs to a .csv file
#==============================================================================
##
## Tested with python 2.7
##
## Copyright (c) 2012, Exosite LLC
## All rights reserved.
##

import sys,time 
from datetime import datetime
from onepv1lib.onep import OnepV1
from onepv1lib.exceptions import *

WINDOW = 50000 # in seconds
FILE = "archive_data.csv"

conn = OnepV1()

#===============================================================================
def __validateArgs():
#===============================================================================
  if len(sys.argv) < 5:
    print "python",sys.argv[0], "CIK ALIAS SINCE UNTIL"
    print "where CIK: one platform client key"
    print "    ALIAS: dataport alias"
    print "    SINCE: MM/DD/YYYY"
    print "    UNTIL: MM/DD/YYYY"
    sys.exit(1)
  cik, alias, since, until = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
  if len(cik) != 40:
    print "Invalid cik"
    sys.exit(1)
  since = since + " 00:00:00"
  until = until + " 23:59:59"
  try:
    start = datetime.strptime(since, "%m/%d/%Y %H:%M:%S")
    end   = datetime.strptime(until, "%m/%d/%Y %H:%M:%S")
  except ValueError as err:
    print "Invalid time format."
    sys.exit(1)
  start_timestamp = int(time.mktime(start.timetuple()))
  end_timestamp = int(time.mktime(end.timetuple()))
  if start_timestamp > end_timestamp:
    print "SINCE must not be greater than UNTIL"
    sys.exit(1)
  return cik, alias, start_timestamp, end_timestamp

#===============================================================================
def __getRID(cik, alias):
#===============================================================================
  try:
    status, rid = conn.lookup(cik, "alias", alias)
    if not status:
      print "Failed to lookup alias: '%s', Reason: %s" % (alias, rid)
      sys.exit(1)
    else:
      return rid
  except OnePlatformException,e:
    print e.message
  except Exception,e:
    print e.message
  return None

#===============================================================================
def __read(cik, alias, since, until):
#===============================================================================
  limit = until - since + 1
  try:
    status, msg = conn.read(cik, rid, options={"starttime":since, "endtime":until, "limit":limit, "sort":"asc"})
    if status:
      return msg
  except:
    print "Failed to read data."
  sys.exit(1)

#===============================================================================
if __name__ == '__main__':
#===============================================================================
  cik, alias, since, until = __validateArgs()
  rid = __getRID(cik, alias)
  if rid:
    file = open(FILE, 'w+')
    limit = until - since
    count = limit/WINDOW + 1
    for i in range(0, count):
      start = since + i * WINDOW
      if i == count-1:
        end = until
      else:
        end = since + (i+1) * WINDOW - 1
      msg = __read(cik, alias, start, end)
      for entry in msg:
        time, data = entry
        line = str(time) + "," + str(data) + "\n"
        file.write(line)
    file.close()
