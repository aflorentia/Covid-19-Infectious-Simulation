# # myls.py
# # Import the argparse library
# import argparse
# import numpy as np
#
# import os
# import sys
#
# # Create the parser
# my_parser = argparse.ArgumentParser(description='List the content of a folder')
#
# # Add the arguments
# my_parser.add_argument('Path',
#                        metavar='path',
#                        type=str,
#                        help='the path to list')
# my_parser.add_argument('-l',
#                        '--long',
#                        action='store_true',
#                        help='enable the long listing format')
#
# # Execute parse_args()
# args = my_parser.parse_args()
# print("You passed "+(str)(len(sys.argv)-1)+" arguments");
#
#
# input_path = args.Path
#
# if not os.path.isdir(input_path):
#     print('The path specified does not exist')
#     sys.exit()
#
# for line in os.listdir(input_path):
#     if args.long:  # Simplified long listing
#         size = os.stat(os.path.join(input_path, line)).st_size
#         line = '%10d  %s' % (size, line)
#     print(line)