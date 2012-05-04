from distutils.core import setup

setup(
    name = "django-weekday-field",
    version = "0.1.3",
    description = "Weekday field for django models",
    url = "http://bitbucket.org/schinckel/django-weekday-field/",
    author = "Matthew Schinckel and Andrew Gall",
    author_email = "matt@schinckel.net and housepage@gmail.com",
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
