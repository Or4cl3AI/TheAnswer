# django_app/django_app/apps.py

```python
from django.apps import AppConfig

class DjangoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_app'
```

Note: The code above is a standard Django AppConfig class that defines the configuration for the Django app. The `default_auto_field` attribute specifies the default primary key field type for models, and the `name` attribute specifies the name of the app.