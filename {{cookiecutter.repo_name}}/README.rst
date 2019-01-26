# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## Features

* TODO

## Usage

### Creating a virtual environment

```
$ make create_environment
$ conda activate {{cookiecutter.repo_name}}
$ make requirements
```

### Updating dependencies

First, add your dependency to `environment.yml`. Then do a
```
$ make requirements
```

### Running your app

This assumes [Kivy] is installed correctly on your system.

```
$ cd {{cookiecutter.repo_name}}
$ python main.py
```

### Deploying to IOS
This makes use of [buildozer], [kivy-ios], and Apple's XCode:

Choose one of the following identities:
```
buildozer ios list_identities
```
and add it to `buildozer.spec` as the value of the
`ios.codesign.debug` (or `ios.codesign.release`) key

```
make ios_release   # fails. That's ok
make xcode         # select your signing credentials and exit
make ios_release   # Fails on the final step: (-exportformat IPA). Ignore this
make xcode
```
now, press play in XCode to build and/or deploy your app

### Running tests

Run its testsuite either with Python3::

    cd {{cookiecutter.repo_name}}
    python -m unittest discover

Or with [nose]:

    cd {{cookiecutter.repo_name}}
    nosetests

Or with [py.test]:

    cd {{cookiecutter.repo_name}}
    py.test


### Deploying to Android

Not Yet Implemented

## License

{{cookiecutter.repo_name}} is distributed under the terms of a
MIT License

### Issues

Report bugs at https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/issues.


[buildozer]: https://github.com/kivy/buildozer
[kivy-ios]: https://github.com/kivy/kivy-ios
[kivy]: https://github.com/kivy/kivy
[mit]: http://opensource.org/licenses/MIT
[nose]: https://github.com/nose-devs/nose/
[py.test]: http://pytest.org/latest/
