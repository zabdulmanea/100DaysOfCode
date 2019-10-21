# Python PIP
""" Check if PIP is installed
python --version
pip --version
python3 --version
pip3 --version
"""

""" Upgrade PIP version
sudo pip install --upgrade pip
sudo pip3 install --upgrade pip
"""

""" Install PIP
pip install pip
"""

""" Install PIP Package | pip install [name of package]
pip install camelcase
"""

import camelcase
c = camelcase.CamelCase()
txt = "Hello, this is a camel case sentence."
print(c.hump(txt))

""" Remove a Package | pip uninstall [name of package]
pip uninstall camelcase
"""

""" List Packages
pip list
"""
