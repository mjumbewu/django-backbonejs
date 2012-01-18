==================
Django Backbone.js
==================

Django-Backbone.js is a reusable Django application to quickly integrate Backbone.js.  It's a
collection of the Backbone.js toolkit files and template tags to display them.  This application
is based on Ryan Brady's django-bootstrapped (https://github.com/rbrady/django-bootstrapped)

This application depends on django.contrib.staticfiles.

No files from Backbone.js toolkit have been modified and retain their MIT license.

* Note: This app only works on Django 1.3 and newer.

Installation
============

pip install django-backbonejs


Configuration
=============

#. Add the `backbonejs` directory to your Python path.

#. Ensure `django.contrib.staticfiles` is added to your `INSTALLED_APPS` setting.

#. Ensure `django.contrib.staticfiles` is configured properly.

#. Add `backbonejs` to your `INSTALLED_APPS` setting.

#. Run `manage.py collectstatic` to copy the Backbone.js files to your static directory.


Template Usage
=================
This application exposes a few template tags for including the Bootstrap toolkit files.

Load the template tags before usage::

    {% load backbonejs %}


```backbone_js```

Backbone supplies structure to JavaScript-heavy applications by providing models
with key-value binding and custom events, collections with a rich API of
enumerable functions, views with declarative event handling, and connects it all
to your existing application over a RESTful JSON interface::

    {% backbone_js %}

Output::

    <script src="underscore.js" type="text/javascript"></script>
    <script src="backbone.js" type="text/javascript"></script>

* Note: The backbone javascript file has a dependency on the underscore file.

Alternatively, you may just want to include all of the scripts.  If so, just use `all` for the tag arguments::

    {% bootstrap_js all %}
