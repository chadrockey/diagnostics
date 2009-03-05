#!/usr/bin/env python
#
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of the Willow Garage nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

# Author: Kevin Watts

import roslib
import pylab
import cPickle


def plot_key(label, stats):

  # create a list of keys
  #boards = [b for b in stats.keys() if b.count('Smart') > 0]
  boards = [b for b in stats.keys() if b != 'tracked_values']
  boards.sort()

  n = len(boards)
  #print "n=%d" %( n)

  if n == 1:
    for index, board in enumerate(boards):
      pylab.hist(stats[boards[0]][label], 100)

  else:
    for index, board in enumerate(boards):
      print board

      pylab.subplot(4, 4, index + 1)
      pylab.hist(stats[board][label], 100)
      pylab.title(board)

  pylab.show()

def readFile(my_file):
  stats = cPickle.load(my_file)
  keys = stats['tracked_values']
  while(1):
    print "available keys:" + str(keys)
    try:
      key = input("what value would you like to plot?")
      if key in keys:
        plot_key(key, stats)
      else:
        print "Error, key not found"
    except:
      return

if __name__ == '__main__':
  import sys
  inputFile = sys.argv[1] 
  print "processing file: %s" %(inputFile) 
  my_file = file(inputFile, 'rb')
  readFile(my_file)
  my_file.close()