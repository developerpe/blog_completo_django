=====
Ejemplo de Blog con Django 2
=====


Inicio
-----------

1. Clona o descarga este repositorio
2. Inicio sesión con tu cuenta de Google en tu navegador y accede a la siguiente URL
    https://myaccount.google.com/lesssecureapps

  Y activa el permiso de Aplicaciones Menos Seguras

3. Crea tu entorno virtual y una vez lo actives ejecuta el comando:

    pip install -r requirements.txt

4. Dirígete al archivo base.py y coloca tus datos en los parámetros:

    EMAIL_HOST_USER = 'correo@gmail.com'
    EMAIL_HOST_PASSWORD = 'contraseña_gmail'

5. Ejecuta el comando python manage.py makemigrations
6. Ejecuta el comando python manage.py migrate
7. Ejecuta el comando python manage.py createsuperuser para crear un nuevo usuario administrador.
8. Ejecuta el comando python manage.py runserver
