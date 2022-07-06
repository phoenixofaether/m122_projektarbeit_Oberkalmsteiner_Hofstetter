# GENERAL INFO
__author__ =  'Luca Hofstetter'
__teammates__ =  'David Oberkalmsteiner'
__version__ = '1.0.2'
__status__ = 'prototype'
__description__ = 'M122 / LB2 - Script 2'
__date__ = '2022/07/04'

# IMPORTS
import sys, getopt

# MAIN FUNCTION
def main(argv):
    # PARAMETERS
    config_path = ''
    input_file_path = ''
    base_dir_path = ''

    try:
        opts, args = getopt.getopt(argv,"hc:ib",["config_path=","input_file_path=", "base_dir_path"])
    except getopt.GetoptError:
        print('test.py -c <config_path> -i <input_file_path> -b <base_dir_path>')
        sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print('test.py -c <config_path> -i <input_file_path> -b <base_dir_path>')
                sys.exit()
            elif opt in ("-c", "--config_path"):
                config_path = arg
            elif opt in ("-i", "--input_file_path"):
                input_file_path = arg
            elif opt in ("-b", "--base_dir_path"):
                base_dir_path = arg
                print('Config file is "', config_path)
                print('Input file is "', input_file_path)
                print('Base directory is "', base_dir_path)

if __name__ == "__main__":
    print('# ' + '=' * 78)
    print('Author: ' + __author__)
    print('Teammates: ' + __teammates__)
    print('Version: ' + __version__)
    print('Status: ' + __status__)
    print('Date: ' + __date__)
    print('# ' + '=' * 78)
    main(sys.argv[1:])