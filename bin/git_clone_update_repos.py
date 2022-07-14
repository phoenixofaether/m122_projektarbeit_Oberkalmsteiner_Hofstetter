# GENERAL INFO
__author__ = 'David Oberkalmsteiner'
__teammates__ = 'Luca Hofstetter'
__version__ = '1.0.2'
__status__ = 'prototype'
__description__ = 'M122 / LB2 - Script 1'
__date__ = '2022/07/04'

# IMPORTS
import argparse
import os
import configparser
import shutil
#os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import git
import stat
from log_script import Logger


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg


# PARAMETER HANDLING
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config_path', required=True, type=lambda x: is_valid_file(parser, x),
                    help='Pfad zu deinem Konfigurationsfile', metavar="FILE")
parser.add_argument('-i', '--input_file_path', required=True, type=lambda x: is_valid_file(parser, x),
                    help='Pfad zu deinem File, in dem du die GitRepos definiert hast', metavar="FILE")
parser.add_argument('-b', '--base_dir_path', required=True, type=str,
                    help='Pfad zu deinem Base-Verzeichnis, wo die GitRepos hingehören', metavar="FOLDER")

args = parser.parse_args()

# READ & SAVE CONFIGURATION FILE
config = configparser.ConfigParser()
config.sections()
config.read(args.config_path)
log_path = config['Config']['log_path']

# initialize Logger
logger = Logger(log_path, 'Clone & Update script')

# ETHER CLONE OR PULL REPOS FROM LINKS
folderNames = []

file = open(args.input_file_path, "r", encoding='utf-8')
for line in file:
    (githubLink, folderName) = line.split(' ')
    folderNames.append(folderName.strip())
    folderPath = os.path.join(args.base_dir_path, folderName).strip()

    if(os.path.exists(folderPath)):
        repo = git.Repo(folderPath)
        o = repo.remotes.origin
        o.pull()
        logger.log('Pulled ' + folderPath)
        repo.__del__()
        continue
    else:
        os.makedirs(folderPath)
        logger.log('Created ' + folderPath)
    repo = git.Repo.clone_from(githubLink, folderPath)
    logger.log('Cloned ' + folderPath + ' from ' + githubLink)

# DELETE OTHER/OLD DIRECTORIES
dirs = os.listdir(args.base_dir_path)
for dir in dirs:
    dirName = dir.strip()
    if not dirName in folderNames:
        fullPath = os.path.join(args.base_dir_path, dirName)
        for root, dirs, files in os.walk(fullPath):
            for dir in dirs:
                os.chmod(os.path.join(root, dir), stat.S_IRWXU)
            for file in files:
                os.chmod(os.path.join(root, file), stat.S_IRWXU)
        shutil.rmtree(fullPath)
        logger.log('Deleted ' + dirName)
