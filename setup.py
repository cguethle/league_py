""" Setup file for league_py """

from setuptools import setup

setup(
      name='league_py',
      version='0.0.1',
      description='Yet another League Of Legends API wrapper.',
      url='http://github.com/cguethle/league_py',
      author='Chris Guethle',
      author_email='chris.guethle@gmail.com',
      license='MIT',
      packages=['league_py'],
      package_dir={'': 'src'},
      install_requires=[
            'requests==2.9.1',
            'pytz==2015.7',
            'gevent'
      ],
      zip_false=False
)
