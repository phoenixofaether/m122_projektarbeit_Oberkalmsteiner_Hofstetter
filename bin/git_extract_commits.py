import argparse
import os
import git

parser = argparse.ArgumentParser()
parser.add_argument('--config_path', help='configuration path')
parser.add_argument('--input_file_path', help='input file path')
parser.add_argument('--base_dir_path', help='base directory path')
args = parser.parse_args()


print('Config file is "', args.config_path)
print('Input file is "', args.input_file_path)
print('Base directory is "', args.base_dir_path)




files = os.listdir(args.base_dir_path)


for folderName in files:
    g = git.Git(args.base_dir_path + folderName)
    loginfo = g.log()
    print(loginfo)
