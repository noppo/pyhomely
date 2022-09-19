#required packages
py -m pip install build twine

#build the package
py -m build

#upload package to testPypi
twine upload -r testpypi dist/*