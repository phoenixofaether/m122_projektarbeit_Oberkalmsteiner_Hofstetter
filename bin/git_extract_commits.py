# GENERAL INFO
__author__ = 'Luca Hofstetter'
__teammates__ = 'David Oberkalmsteiner'
__version__ = '1.0.3'
__status__ = 'production'
__description__ = 'M122 / LB2 - Script 2'
__date__ = '2022/07/14'


# imports
from git import Repo
from datetime import datetime
from log_script import Logger
import os
import argparse


# function dateConverter: Convert a date to desired format
def dateConverter(date):
    return(date.strftime("%m%d%Y"))

lines = []

# Parser arguments: output, log, base_dir_path
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output_file", help="File with output inside", default="commits.txt")
parser.add_argument("-b", "--base_dir_path", help="Directory with git-repos inside")
parser.add_argument("-l", "--log_path", help="Path to log-file", default="log.log")
args = parser.parse_args()

# logger instance
logger = Logger(args.log_path, 'Git extract commits')

# log base_dir_path error
if not os.path.exists(args.base_dir_path):
    logger.log("Error:" + args.base_dir_path + " doesn't exist!")

subDirs = os.listdir(args.base_dir_path)

# loop through every sub-directory
for subdir in subDirs:
    dir = os.path.join(args.base_dir_path, subdir)
    # check if directory exists
    if os.path.exists(dir):

        # creates new repository
        repos = Repo(dir)
        logger.log("Following directory is currently in usage: " + dir)

        # creates commit list
        commits = list(repos.iter_commits())

        # format commit data in desired format
        for commit in commits:
            lines.append(subdir + "," + dateConverter(commit.authored_datetime) + "," + str(commit.hexsha) + "," + str(commit.author))
    else:
        logger.log("Directory doesn't exist :" + dir)

# fill output-file with formated commits
f = open(args.output_file, "w")
f.write("Zielverzeichnis,Datum,Commit-Hash,Author \n")
for line in lines:
    f.write(line + "\n")
f.close()

logger.log("Successfully writen commit to text-file.")
