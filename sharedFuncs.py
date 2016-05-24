import os
import sys
import json

ROOTDIR = '.'
ENVFILE = '.gitEnvironments'
ENVIRONMENTS = 'Environments'
REPOS = 'repos'

def loadEnvs():
  existingEnv = {ENVIRONMENTS: dict()}
  if os.path.isfile(ENVFILE):
    with open(ENVFILE) as jsonFile:
      existingEnv = json.load(jsonFile)
  return existingEnv[ENVIRONMENTS]