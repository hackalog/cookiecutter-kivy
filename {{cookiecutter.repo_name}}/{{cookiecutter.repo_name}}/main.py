#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
from {{cookiecutter.class_name|lower}} import {{cookiecutter.class_name}}App

kivy.require('{{cookiecutter.minimum_kivy_version}}')

__version__ = "{{cookiecutter.version}}"

if __name__ == "__main__":
    {{cookiecutter.class_name}}App().run()
