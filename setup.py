from setuptools import setup
setup(
    name='scalepy',
    description='Provies renaming utility for Nikon output files.',
    version='0.1',
    url='https://github.com/ChrisoftheBoyerClan/scale.py',
    author='Christopher Boyer',
    author_email='ChrisoftheBoyerClan@gmail.com',
    entry_points={ 'console_scripts': [ 'scalepy=scale.scale:main', ], },
    packages=['scalepy'],
    license='MIT',
    keywords='scale image resize'
)