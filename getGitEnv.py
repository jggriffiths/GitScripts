#!/usr/local/bin/python

import os
import collections
import argparse
import sharedFuncs as shared
from git import Repo
join = os.path.join

from git import RemoteProgress

class MyProgressPrinter(RemoteProgress):
  def update(self, op_code, cur_count, max_count=None, message=''):
    print(op_code, cur_count, max_count, cur_count / (max_count or 100.0), message or "NO MESSAGE")

def loadParser():
  parser = argparse.ArgumentParser()
  parser.add_argument("envName", help = "name of the environment to get", default = None, nargs = "?")
  parser.add_argument("-l", "--list",help = "list all of the stored environments", action = "store_true" )
  parser.add_argument("-p", "--pull",help = "auto pull from remote when switching branch", action = "store_true")
  return parser

parser = loadParser()
args = parser.parse_args()
envs = shared.loadEnvs()
if args.envName:
  print "Fetching environment: " + args.envName
  targetEnv = envs.get(args.envName, None)
  if targetEnv != None:
    print 'Found Target Env: ' + args.envName
    for dir in targetEnv[shared.REPOS]:
      print 'Repo: ' + dir
      branchName = targetEnv[shared.REPOS][dir]
      print 'Branch: ' + branchName
      repo = Repo(join(shared.ROOTDIR, dir))
      #origin = repo.remotes.origin
      #origin.fetch()
      #repo.heads[branchName].checkout()*/
      repo.git.fetch()
      repo.git.checkout(branchName)
      if args.pull:
        repo.git.pull()
elif args.list:
  orderedEnvs = collections.OrderedDict(sorted(envs.items()))
  for env in orderedEnvs:
    print env
else:
  parser.print_help()
  exit()
  
print 'Done.';
