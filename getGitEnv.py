#!/usr/local/bin/python

import os
import sys
import json
from git import Repo
join = os.path.join

from git import RemoteProgress

class MyProgressPrinter(RemoteProgress):
  def update(self, op_code, cur_count, max_count=None, message=''):
    print(op_code, cur_count, max_count, cur_count / (max_count or 100.0), message or "NO MESSAGE")


ROOTDIR = '.'
ENVFILE = '.gitEnvironments'
ENVIRONMENTS = 'Environments'
REPOS = 'repos'

if len(sys.argv) < 2:
  print 'Format:\n' + '$ python ' + sys.argv[0] + ' <environment name> <options>'
  print '\n'
  print 'Options:'
  print '-p\tautomatically pulls'
  print '-l\list environments'
  exit()

autopull = False
listEnv = False
for arg in sys.argv:
  if arg == "-p":
    autopull = True
  if arg == '-l':
    listEnv = True

envName = sys.argv[1]
print 'Fetching environment ' + envName

existingEnv = {ENVIRONMENTS: dict()}
if os.path.isfile(ENVFILE):
  with open(ENVFILE) as jsonFile:
    existingEnv = json.load(jsonFile)

for environment in existingEnv[ENVIRONMENTS]:
  if not listEnv and environment == envName:
    for dir in existingEnv[ENVIRONMENTS][environment][REPOS]:
      print 'Repo: ' + dir
      branchName = existingEnv[ENVIRONMENTS][environment][REPOS][dir]
      print 'Branch: ' + branchName
      repo = Repo(join(ROOTDIR, dir))
      #origin = repo.remotes.origin
      #origin.fetch()
      #repo.heads[branchName].checkout()*/
      repo.git.fetch()
      repo.git.checkout(branchName)
      if autopull:
        repo.git.pull()
    exit()
  else:
      print environment

print 'Done.';
