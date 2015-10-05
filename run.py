import os
name  = raw_input(' Enter name')
os.system('mkdir '+name)
os.system('mkdir '+name+'/'+name)
os.system('touch '+name+'/'+name+'/__init__.py')

ver  = raw_input(' Enter version')
desc  = raw_input(' Enter description')
githuburl = raw_input('Enter github url')
author = raw_input('enter author')
email  = raw_input('Enter email')

code = '''
from setuptools import setup

setup(name="'''+name+'''",
	version="'''+ver+'''",
	description="'''+desc+'''",
	url="'''+githuburl+'''",
	author="'''+author+'''",
	author_email="'''+email+'''",
	license='MIT',
	packages=["'''+name+'''"],
	zip_safe=False)
'''

with open(name+'/setup.py', "w") as text_file:
	text_file.write(code) 
	os.system('mkdir '+name+'/bin')
	script_path = raw_input('Path of python script file')

with open(script_path, 'r') as content_file:
	content = content_file.read()

with open(name+'/bin/'+name, "w") as text_file:
	text_file.write('#!/usr/bin/env python \n')
	text_file.write(content)
os.chdir(name+'/')
os.system('python setup.py register sdist upload')

