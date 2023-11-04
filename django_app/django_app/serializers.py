# Django App

Here is the code for the file `django_app/django_app/serializers.py`:

```python
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
```

This code defines a serializer class `UserSerializer` that serializes the `User` model from the `django.contrib.auth.models` module. The serializer includes the `id`, `username`, and `email` fields of the `User` model.

Please let me know if you need any further assistance.