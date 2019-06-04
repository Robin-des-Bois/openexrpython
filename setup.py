from distutils.core import setup
from distutils.extension import Extension
from distutils.command.build_py import build_py as _build_py

from os import system, environ

from distutils.core import setup, Extension

conda_env_path = environ['CONDA_PREFIX']

assert conda_env_path is not None and len(conda_env_path) > 0, 'This setup.py is patched to work with conda environements see (https://github.com/openexr/openexr/issues/207#issuecomment-478425804)' 

version = "1.3.2"
setup(name='OpenEXR',
  author = 'James Bowman',
  author_email = 'jamesb@excamera.com',
  url = 'http://www.excamera.com/sphinx/articles-openexr.html',
  description = "Python bindings for ILM's OpenEXR image file format",
  long_description = "Python bindings for ILM's OpenEXR image file format",
  version=version,
  ext_modules=[ 
    Extension('OpenEXR',
              ['OpenEXR.cpp'],
              include_dirs=[conda_env_path + '/include/OpenEXR'],
              library_dirs=[conda_env_path + '/lib'],
              libraries=['Iex', 'Half', 'Imath', 'IlmImf', 'z'],
              extra_compile_args=['-g', '-DVERSION="%s"' % version])
  ],
  py_modules=['Imath'],
)
