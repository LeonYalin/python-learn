from ..util import print_cmd


def creating_packages():
    print_cmd('Nesting modules', """
    - In python, the app divided into packages with modules. Package in like a Java package (folder like), and a module is a single python file.
    - Package has the __path__ property that holds the package path

    - If the REPL doesn't recognize the path, we can add it manually: sys.path.append('folder_name')
    - Other options is to expor it via bash variable: EXPORT PYTHONPATH=folder_name
    """)


def using_packages():
    print_cmd('Using packages', """
    The __file__ property holds the __init__.py file path.
    When a package is imported, the __init__.py is being executed. We can see it by placing print statement there.
    To run a module from a command line, use "python -m package_name.module_name"

    Import synthax:
    from package import module1, module2
    from .. import module1

    Using __all__
    The __all__ contains list of all public exports of the module(without underscores) when import * is used
    If not specified, all functions will be public
    Hint: use print(locals()) to view all local available variables

    Example of __init__.py with __all__:
    from package.module import func1 as f1
    from package2.module2 import func2 as f2
    __all__ = ['f1', 'f2']
    """)


def namespaces_and_executable_packages():
    print_cmd('Namspaces and executable packages', """
    Namespace packages:
    These packages are splitted across multiple files and do not have the __init__,py file.

    Sharing namespaces:
    In order to share namespaces, we should organize code in separate folders with same names.
    When importing, python will understand from which folder to import

    Executable directories:
    To make a directory executable (directory, not package), create a __main__.py file in it.

    Executable .zip files:
    Works same way as with directories, but we should zip the contents of the directory (not the directory itself).
    This is an analog to .jar files in Java

    Executable packages:
    Same as with directories, but called with the -m flag, e.g. python -m package_dir
    """)


def recommended_package_layout():
    print_cmd('Recommended package layout', """
    Python package shhould consist of:
    - root directory (not package),
    - README.rst file(README.MD analog), setup.py
    - Common directories at the root level: docs/, src/, tests/ 
    - Main app package inside src/

    Setup.py example: (package.json analog)

    import setuptools

    setuptools.setup(
        name='project_name,
        version='1.0.0',
        packages=setuptools.find_packages('src'),
        package_dir={'': 'src'})

    Implementing Pligins:
    There are 2 ways to implement plugins: with Namespace Packages and with setuptools.py
    First implementation uses the library pkgutil and importlib libraries to add modules
    Second extents setup.py options using setuptools extension points

    Package distribution:
    We use PyPi - Python Package index to share paxkages (npm analog). Than, we can install it using "pip install package_name"

    There are two kinds of packages: "Built" and "Source" packages.
    - Built package can be placed directly into python directory and it is ready to use
    - Package format can be .zip, .tar or .whl (wheel).
    - The command "bdist" is used to build a built package. Also, the "whell" package need to be installe first

    - Source packages contain al the sources for the package, and can be built (a.k.a complied) using different configurations due to our needs.
    - The command "sdist" is used to build the source package

    To upload a package to the PyPi, we need to use the "twine" package.
    Than, we use "twine upload package_name" to upload the package
    """)


def organizing_larger_programs_main():
    creating_packages()
    using_packages()
    namespaces_and_executable_packages()
    recommended_package_layout()