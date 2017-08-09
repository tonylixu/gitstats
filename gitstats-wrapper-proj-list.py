from __future__ import print_function
from __future__ import absolute_import
'''A gitstats wrapper which calls gitstats recursively on directory 
that contains multiple git repositories, based on a project.list file.
    Usage:
      # python gitstats-wrapper.py source_dir dest_dir
    Note:
        A .repo/project.list is required
'''
import argparse
import os
import os.path
import time
from gitstats import GitStats


# Initialize a GitStats class
g = GitStats()

# Parse command line arguments, retrieve the source directory
# and the output directory
# Instantiate the parser
parser = argparse.ArgumentParser(description='gitstats wrapper')
# Add required positional argument
parser.add_argument('project_dir', help='The absolute path of project folder, i.e /home/gschultz/8956n/')
parser.add_argument('dest_dir', help='The output folder')

# Parse the command line arguments
args = parser.parse_args()
project_dir = args.project_dir
dest_dir = args.dest_dir
projects = []
# Get the project list file
project_list_file = project_dir + '.repo/project.list'
# Open and read all the projects
with open(project_list_file, 'r') as lines:
    for line in lines:
        #line = project_dir + line
        projects.append(line.rstrip('\n'))

# Call gitstats on each project
for p in projects:
     if p != '.':
         project_path = project_dir + p
         project_out = dest_dir + p
         print('Going to run gitstats on {0}'.format(project_path))    
         print('Output will be in {0}'.format(project_out))
         time.sleep(5)
         g.run([project_path, project_out])
