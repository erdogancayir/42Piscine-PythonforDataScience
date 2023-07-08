Directory structure: Organize your code and related files in the following directory structure:

```
ft_package/
├── ft_package/
│   ├── __init__.py
│   └── count_in_list.py
├── setup.py
└── README.md

```

#### Building the package: Navigate to the root directory (ft_package) and run the following command to build your package:
```python setup.py sdist bdist_wheel```<br>
This will create a source distribution (dist/ft_package-0.0.1.tar.gz) and a binary wheel distribution (dist/ft_package-0.0.1-py3-none-any.whl).
#### Installing and testing your package: You can now install your package with pip:
```pip install ./dist/ft_package-0.0.1.tar.gz``` <br>
or <br>
```pip install ./dist/ft_package-0.0.1-py3-none-any.whl``` <br>
After this, you should be able to import your package and use the count_in_list function in Python scripts:
```from ft_package import count_in_list
print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
”print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
```
You can also check if your package is installed and its details by running pip show -v ft_package.

Please note, if you want your package to be available for others to install via PyPI (Python Package Index), you will need to upload your package there. This involves creating an account and following the upload instructions. However, this step is not necessary if you just want to create a package for local use or distribution.
