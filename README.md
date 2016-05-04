# GitScripts
Currently, for a project, a developer may need multiple git repositories for a project.  This presents a problem when having to switch between multiple tasks across these repositories.

A team member suggested “git environments” for our collection of repositories.  Basically, a way of saving off and setting up the repositories for a current task.  I thought I’d give implementing it a try.


‘setGitEnv.py’ -> scans the current directory for git repositories and saves the directory and current branch to a .gitEnvironments file

		Called via “setGitEnv.py <Environment Name> <options>”
			Options:
				-f	overwrites an environment of the same name

‘getGetEnv.py’ -> pulls an environment from the .gitEnvironments file and then attempts to checkout the associated branch

		Called via “getGitEnv.py <Environment Name> <options>”
			Options:
				-p	automatically pulls after switching branches


Requires gitpython:   ‘pip install gitpython’


This has not been thoroughly tested.  Suggestions for options and features and bug fixes are welcome.
