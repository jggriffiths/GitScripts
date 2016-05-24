#!/usr/local/bin/python

import os
import sys
import json
import argparse
from git import Repo
join = os.path.join

ROOTDIR = '.'
ENVFILE = '.gitEnvironments'
ENVIRONMENTS = 'Environments'
REPOS = 'repos'

def loadParser():
  parser = argparse.ArgumentParser()
  parser.add_argument("envName", help = "name of the environment to save", action = "store")
  parser.add_argument("-f", "--overwrite", help = "overwrites existing environment", action = "store_true")
  parser.add_argument("-d", "--dryrun", help = "only print existing environment setup", action = "store_true")
  return parser
  
def loadEnvs():
  existingEnv = {ENVIRONMENTS: dict()}
  if os.path.isfile(ENVFILE):
    with open(ENVFILE) as jsonFile:
      existingEnv = json.load(jsonFile)
  return existingEnv[ENVIRONMENTS]

parser = loadParser()
args = parser.parse_args()

print 'Creating environment ' + args.envName

repos = {}
for dir in next(os.walk(ROOTDIR))[1]:
  repo = Repo(dir)
  repos[dir] = str(repo.active_branch);
  print 'Found: ' + dir + ' => ' + str(repo.active_branch)

if args.dryrun:
  exit()

envs = loadEnvs()
targetEnv = envs.get(args.envName, None)
if targetEnv and not args.overwrite:
    print 'Environment ' + args.envName + ' already exists.  Execute with "-f" to overwrite'
    exit()
  
newEnv = {REPOS: repos}
envs[args.envName] = newEnv
with open(ENVFILE, 'w+') as outfile:
    json.dump({ENVIRONMENTS: envs}, outfile)