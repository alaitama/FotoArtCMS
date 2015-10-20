from setuptools import setup

setup(name='FotoArtCMS',
      version='1.0',
      description='OpenShift App',
      author='Alberto Laita',
      author_email='alblaita@gmail.com',
      url='http://www.python.org/sigs/distutils-sig/',
#      install_requires=['Django>=1.3'],
      install_requires=[
          'Django==1.6.5',
          'Mezzanine==3.1.4',
          'django_compressor==1.5',
          'django-storages==1.1.8',
          'boto==2.38.0'
      ],
     )
