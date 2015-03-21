#!/bin/python

import os
import pexpect
import sys


AUTOOL_URL = "/home/ext-huaqin-liuzhigang/liudoc/autool_python"
REPO_REV = "master"

my_autool = "~/.autool/autool"
my_autool_dir = "~/.autool"
my_main = "~/.autool/main.py"


def _Run(s):
    # pexpect.spawn(s, logfile=sys.stdout)
    pexpect.run(s, logfile=sys.stdout)


def _Find_autool():
    if os.path.isdir(my_autool_dir) and os.path.isfile(my_autool) \
            and os.path.isfile(my_main):
        return True
    else:
        print """there is no autool in your ~/.autool
begin to download autool
        """

        return False


def _Make_dir_file():
    if not os.path.isdir(my_autool_dir):
    	try:
        	os.makedirs(my_autool_dir)
    	except OSError as e:
        	print "can not make %s directory:%s" % (my_autool_dir, e.strerror)


def _Autool_clone():
    try:
        _Run("git clone %s %s" % (AUTOOL_URL, my_autool_dir))
    except Exception as e:
        print "failue to clone: %s" % e
        sys.exit(1)


def _Autool_pull():
    try:
    	os.chdir(my_autool_dir)
        _Run("git pull")
    except Exception as e:
        print "failue to pull: %s" % e
        sys.exit(1)


def main():
    if _Find_autool():
        _Run("python %s" % my_main)
    else:
        _Make_dir_file()
        _Autool_clone()
    _Autool_pull()
    # _Run("python %s" % my_main)


if __name__ == '__main__':
    main()
