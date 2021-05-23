<h1>Django: signup, login and logout</h1>

<i>A little tutorial on how to configure the features of:
signup, login and logout with django and Django Rest Framework</i>


<h3>Install Django</h3>
<p>
<code>pip install django</code>

or specifying the version   
<code>pip install django==3.0</code>

install django rest framework   
<code>pip install djangorestframework</code>   
<i>Remember to add <code>'rest_framework'</code> in INSTALLED_APPS, inside the <b>settings.py</b> file </i>
</p>

<h3>Create Django Project</h3>
Into the project folder:
<p>
<code>django-admin startproject name .</code>

Within the name folder the files will be created:
<ul>
    <li><b>settings.py</b>,  controls the project settings</li>
    <li><b>urls.py</b>, to build in response to a browser or URL request</li>
    <li><b>wsgi.py</b>, Web Server Gateway Interface</li>
    <li><b>manage.py</b>, to execute various Django commands</li>
</ul>

<h3>Create Django App</h3>
<p>
<code>django-admin startapp name .</code>

<i>Remember to add the created app <code>'name'</code> in INSTALLED_APPS, inside the <b>settings.py</b> file </i>

Within the name folder the files will be created:
<ul>
    <li><b>admin.py</b>, configuration for the Admin app integrated in Django</li>
    <li><b>apps.py</b>, configuration for the app</li>
    <li><b>migrations</b>, keeps track of changes made in models.py, so that it is synchronized with the DB</li>
    <li><b>models.py</b>, where models are defined.A model is a class that represents 
    a table in the DB and where each class attribute is a table field</li>
    <li><b>tests.py</b>,app-specific tests</li>
    <li><b>views.py</b>, the request/response logic is managed</li>
</ul>


<h3>Create superusers</h3>
<p>
<code>python manage.py createsuperuser</code>

The most powerful user with permissions to create, read, update and delete data in the Django admin
</p>

<h3>Django Commands</h3>
<ul>
    <li><code>python manage.py makemigrations</code>, when you want make change to a model</li>
    <li><code>python manage.py migrate</code>, when new migrations are available that have not yet been applied to the data in the current instance</li>
    <li><code>python manage.py runserver</code>, to run the local server</li>

</ul>


<h3>Models.py</h3>
<p>
We use the Django’s built-in authentication system, it fits most of the use cases and is very safe.
We create a new Django Model to store the extra information that relates to the User Model

Name the Django Model as <code>User</code>

User model will be automatically created/updated when we create/update User instances.
Everything is done (like saving) through the User model.

<a href="https://docs.djangoproject.com/en/3.2/ref/contrib/auth/"> Django.contrib.auth documentation </a>
<br>
<a href="https://docs.djangoproject.com/en/3.2/topics/db/examples/one_to_one/"> One-to-one relationships documentation </a>
</p>


<h3>Serializers.py</h3>
<p>
It facilitates the conversion of complex data 
to native Python data types that can be rendered using JSON or XML

Create <code>serializers.py</code> file in the app folder and indicate that all fields in the model should be used

<code>create</code> function to save the password.

Raw passwords are not stored, Django provides a flexible password storage system and uses PBKDF2 by default

<a href="https://docs.djangoproject.com/en/3.2/topics/serialization/">Serializing Django objects documentation </a>
</p>


<h3>Views.py</h3>
<p>
Create API view

We handle incoming json requests and validate it to confirm that all required fields are correct
</p>