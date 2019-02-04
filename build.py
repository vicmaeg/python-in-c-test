#Build script, obtains the configuration from the following environment variables:

# CC: The compiler to be used
# CFLAGS: The CFLAGS to be used
# LDFLAGS: The LDFLAGS to be used
# LD_LIBRARY_PATH: Extra libraries paths
# C_INCLUDE_PATH: Extra include paths
# PYTHON_LDFLAGS: path to PythonXX.lib
# PYTHON_INCLUDE_PATH: The path to Python.h
# PYTHON_DLL_PATH: The path to PythonXX.dll, depending on the version of python you want to use

import os
import sys
import subprocess

def build (python_path):
    print ("Start building the CPython wrapper...")
    python_include_path = os.path.join (python_path, "include")
    python_lib_dll = os.path.join (python_path, "Python35.dll")
    compiler = os.environ['CC']
    print ("Generating test.o")
    subprocess.run ([compiler, "-c", "test.c", "-o", "test.o",
                    "-I", python_include_path],
                    check=True)
    print ("linking with %s" % python_lib_dll)
    subprocess.run ([compiler, "-o", "test", "test.o", python_lib_dll], check=True)
    
if __name__ == "__main__":
    if sys.version_info < (3, 5):
        print ("Incorrect version of Python, please use Python 3.5 or greater")
        exit (-1)
    print ("Python version detected is: %s" % sys.version)
    print ("Python executable path is: %s" %sys.executable)
    python_path, filename = os.path.split (sys.executable)
    print ("Python path detected is: %s" % python_path)
    build (python_path)

    




