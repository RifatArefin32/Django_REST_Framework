# Create Project
The following command is used to create a project of the current directory. Usually we create project in root directory.
```bash
django-admin startproject django_rest_framework .
```

# Create an App Package
- Create a directory, suppose `apps`
- Create an `__init__.py` file which is important to make the dirctory as package


# Create an App under a Package
- Go to the package directory `apps` and create an app `accounts`
```bash
django-admin startapp accounts
```
- After creating the accounts app, update app name with package at `accounts/apps.py` in `package_name.app_name` format i.e. `apps.accounts`
- Add the app name `accounts` in `INSTALLED_APPS` array at `django_rest_framework/settingss.py`