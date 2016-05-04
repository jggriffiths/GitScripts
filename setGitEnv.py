#!/usr/local/bin/python

import os
import sys
import json
from git import Repo
join = os.path.join

ROOTDIR = '.'
ENVFILE = '.gitEnvironments'
ENVIRONMENTS = 'Environments'
REPOS = 'repos'

if len(sys.argv) < 2:
  print 'Command format\n' + '$ python ' + sys.argv[0] + ' <environment name>'
  print '\n'
  print 'Options:'
  print '-f\toverwrites exsiting environment'
  exit()

envName = sys.argv[1]
print 'Creating environment ' + envName

overwrite = False
for arg in sys.argv:
  if arg == "-f":
    overwrite = true;

repos = {}
for dir in next(os.walk(ROOTDIR))[1]:
  repo = Repo(dir)
  repos[dir] = str(repo.active_branch);
  print 'Found: ' + dir + ' => ' + str(repo.active_branch)

existingEnv = {ENVIRONMENTS: dict()}
if os.path.isfile(ENVFILE):
  with open(ENVFILE) as jsonFile:
    existingEnv = json.load(jsonFile)

for environment in existingEnv[ENVIRONMENTS]:
  if environment == envName and not overwrite:
    print 'Environment ' + envName + ' already exists.  Execute with "-f" to overwrite'
    exit()

newEnv = {REPOS: repos}
existingEnv[ENVIRONMENTS][envName] = newEnv
with open(ENVFILE, 'w+') as outfile:
    json.dump(existingEnv, outfile)
