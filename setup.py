from distutils.core import setup

setup(
    name = "django-weekday-field",
    version = "1.0",
    description = "Weekday field for django models",
    url = "http://bitbucket.org/schinckel/django-weekday-field/",
    author = "Matthew Schinckel",
    author_email = "matt@schinckel.net",
    packages = [
        "weekday_field",
    ],
    classifiers = [
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
    ],
)
