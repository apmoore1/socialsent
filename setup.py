from setuptools import setup, find_packages

setup(name='socialsent',
      version='0.1.2',
      description='Algorithms for inducing domain-specific sentiment lexicons from unlabeled corpora.',
      url='https://github.com/williamleif/socialsent',
      packages=find_packages(),
      author='William Hamilton',
      author_email='wleif@stanford.edu',
      license='Apache Version 2',
      #packages=['socialsent'],
      install_requires = ['backports.weakref==1.0rc1',
                          'bleach==1.5.0',
                          'cycler==0.10.0',
                          'html5lib==0.9999999',
                          'Keras==2.0.5',
                          'Markdown==2.2.0',
                          'matplotlib==2.0.2',
                          'nltk==3.2.4',
                          'numpy==1.13.0',
                          'protobuf==3.3.0',
                          'pyparsing==2.2.0',
                          'python-dateutil==2.6.0',
                          'pytz==2017.2',
                          'PyYAML==3.12',
                          'scikit-learn==0.18.2',
                          'scipy==0.19.1',
                          'six==1.10.0',
                          'tensorflow==1.2.0',
                          'Theano==0.9.0',
                          'Werkzeug==0.12.2'],
      package_data= {'socialsent' : ['data/lexicons/*.json']},
      zip_safe=False)
