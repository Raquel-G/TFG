from setuptools import setup

setup(name='autopentest',
      version='0.1.0',
      packages=['autopentest'],
      entry_points={
          'console_scripts': [
            'autopentest = autopentest.__main__:main'
        ],
        'gui_scripts': [
            'baz = my_package_gui:start_func',
        ]
      },
      )
