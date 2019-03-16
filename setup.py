try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='exptools',
    # version='0.1.0',
    # author='S. Fenn',
    # author_email='shannon.fenn@gmail.com',
    # # packages=['exptools'],
    scripts=['scripts/j_submit_single.sh'],
    entry_points={
        'console_scripts': [
            'check_run = scripts.check_run:main',
            'check_solo_results = scripts.check_solo_results:main',
            'list_subdirs = scripts.list_subdirs:main',
            'summarise_multiexp = scripts.summarise_multiexp:main',
            'submit_bundled_jobs = scripts.submit_bundled_jobs:main',
            'bundle = scripts.bundle:main',
        ],
    }
    # url='https://github.com/shannonfenn/data-tools',
    # license='LICENSE.txt',
    # description='Tools for data generation and handling.',
    # long_description='',
    # install_requires=[
    #     "numpy >= 1.10.1",
    #     "pandas >= 0.17.0",
    # ],
)
