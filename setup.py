from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='ploneconf2014.contenttypes',
      version=version,
      description="Example Diazo Theme Package",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='contenttypes, package, practica',
      author='Yanina M',
      author_email='yaninamuradas@gmail.com',
      url='https://github.com/Yani18/ploneconf2014.contenttypes.git',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ploneconf2014'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.api',
      ],
      extras_require={
        'test': ['plone.app.testing'],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
