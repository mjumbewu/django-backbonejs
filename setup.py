from setuptools import setup, find_packages

setup(
    name='django-backbonejs',
    version='0.0.1-dev',
    description='A reusable Django application to quickly integrate Backbone.js.',
    long_description=open('README.rst').read(),
    # Get more strings from http://www.python.org/pypi?:action=list_classifiers
    author='Mjumbe Poe',
    author_email='mjumbewu@gmail.com',
    url='https://github.com/mjumbewu/django-backbonejs',
    download_url='https://github.com/mjumbewu/django-backbonejs/downloads',
    license='BSD',
    packages=find_packages(exclude=('ez_setup', 'tests', 'example')),
    # tests are on the roadmap
    #tests_require=[
    #    'django>=1.3,<1.4',
    #],
    #test_suite='runtests.runtests',
    include_package_data=True,
    zip_safe=False, # because we're including media that Django needs
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
