import platform
import os
import sys
import pkg_resources
import json
import yaml
from distutils.sysconfig import get_python_lib

py_info = {}

py_info['version'] = platform.python_version()

py_info['path'] = os.environ['PYTHONPATH']

if 'VIRTUAL_ENV' in os.environ:
    py_info['virtual environment'] = os.environ['VIRTUAL_ENV']
else:
    py_info['virtual environment'] = 'None'

py_info['executable location'] = sys.executable

py_info['site-packages location'] = get_python_lib()

py_info['pip location'] = os.path.join(get_python_lib(), 'pip')

installed_packages = {}

for d in pkg_resources.working_set:
    installed_packages[d.project_name] = d.version


py_info['installed packages'] = installed_packages

with open('pyverse.json', 'w') as json_file:
    json.dump(py_info, json_file, indent=4)

with open('pyverse.yml', 'w') as outfile:
    yaml.dump(py_info, outfile, default_flow_style=False)
