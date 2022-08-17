#### Install the core module in you environment using the following command
```
pip install --force-reinstall 'git+https://github.com/lalitvasoya/django_core_module.git@develop#egg=core&subdirectory=setup'
```

##### Formate the installable link
- `REPO_URL=https://github.com/lalitvasoya/django_core_module.git`
- `BRANCH=develop`
- `EGG=core`
- `SUBDIRECTORY=setup`

> pip install --force-reinstall 'git+`{$REPO_URL}`@`{$BRANCH}`#egg=`{$EGG}`&`{$SUBDIRECTORY}'


When a module has been successfully installed, you must use it in your project by according to the steps below.

- Add `'core'` to your `INSTALLED_APPS` setting.
    ```
    INSTALLED_APPS = [
        ...
        'core',
    ]
    ```

- Migrate your database :boom:
  ```python manage.py migrate```

- enjoy codding :smiley:


#### The file strucure of the core module 
```sh
.
├── core -> setup/core # symbolic link of setup/core app
├── db.sqlite3
├── installable_app
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── setup # installable applications
    ├── core
    │   ├── admin # python module register models 
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── managers # python module contain the managers of models
    │   ├── migrations # python module contian the model migrations
    │   ├── models # python module contain the django models
    │   ├── serializers # python module 
    │   ├── tests.py
    │   └── views.py
    ├── __init__.py
    ├── README.rst
    ├── requirements.txt
    └── setup.py
```
