# Testing python submodules

- Create virtual environment
- Install dependencies
- run "pytest"

### Notes

The most important part of this example is the "conftest.py" file. When pytest discovers a conftest.py, it modifies sys.path so it can import stuff from the conftest module. So, since now an empty conftest.py is found in rootdir, pytest will be forced to append it to sys.path. If you remove this file, you can check that tests don't run correctly.