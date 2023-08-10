"""
Pandas Getting Started

Installation of Pandas
If you have Python and PIP already installed on a system, then installation of Pandas is very easy.

Install it using this command:

#\ will cause error and program not run
'C:users\Your Name>pip install pandas'

If this command fails, then use a python distribution that already has Pandas installed like, Anaconda, Spyder etc.

Import Pandas
Once Pandas is installed, import it in your applications by adding the import keyword:

import pandas
Now Pandas is imported and ready to use.
"""
import pandas as pd

my_dataset = {
        'cars': ["BMW", "Volvo", "Ford"],
        'passings': [3, 7, 2]

}

my_var = pd.DataFrame(my_dataset)

print(my_var)

"""
Checking Pandas Version
The version string is stored under __version__ attribute.
"""
print('\nChecking Pandas version :')
print(pd.__version__)       # 1.4.2
