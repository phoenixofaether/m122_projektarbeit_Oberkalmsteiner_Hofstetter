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
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import git


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
parser.add_argument('-b', '--base_dir_path', required=True, type=lambda x: is_valid_file(parser, x),
                    help='Pfad zu deinem Base-Verzeichnis, wo die GitRepos hingehören', metavar="FILE")

args = parser.parse_args()

# READ & SAVE CONFIGURATION FILE
config = configparser.ConfigParser()
config.sections()
config.read(args.config_path)
log_path = config['Config']['log_path']

file = open(args.input_file_path, "r", encoding='utf-8')
for line in file:
    (githubLink, folderName) = line.split(' ')
    folderPath = os.path.join(args.base_dir_path, folderName).strip()

    if(os.path.exists(folderPath)):
        repo = git.Repo(folderPath)
        o = repo.remotes.origin
        o.pull()
        continue
    else:
        # print(os.path.normpath(folderPath))
        # print('C:\\temp\\Test\\Jerome_Fromherz_Noel_Küng')
        # 'C:\\temp\\Test\\Jerome_Fromherz_Noel_Küng'
        os.makedirs(folderPath)
    repo = git.Repo.clone_from(githubLink, folderPath)
