from setuptools import setup, find_packages

README = open('README.txt').read()

setup(
    name = "django-weekday-field",
    version = "1.1.0",
    description = "Weekday field for django models",
    url = "http://bitbucket.org/schinckel/django-weekday-field/",
    author = "Matthew Schinckel",
    author_email = "matt@schinckel.net",
    packages = find_packages(),
    package_data = {
        '': ['static/*/*/*'],
    },
    classifiers = [
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
    ],
    install_requires=["Django"],
    tests_require=["Django"],
    test_suite="runtests.runtests",
    )
