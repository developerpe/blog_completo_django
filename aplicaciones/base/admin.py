from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class ContactoResource(resources.ModelResource):
    class Meta:
        model = Contacto

class WebResource(resources.ModelResource):
    class Meta:
        model = Web

class RedesSocialesResource(resources.ModelResource):
    class Meta:
        model = RedesSociales

class SuscriptorResource(resources.ModelResource):
    class Meta:
        model = Suscriptor

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre','estado','fecha_creacion')
    search_fields = ['nombre']
    resource_class = CategoriaResource

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre','apellidos','email','descripcion','fecha_creacion')
    search_fields = ['nombre','apellidos','email']
    resource_class = AutorResource

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('titulo','publicado','autor','descripcion','estado','fecha_publicacion')
    search_fields = ['titulo','autor']
    resource_class = PostResource

class WebAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nosotros','email','direccion','telefono','estado','fecha_creacion')
    search_fields = ['email']
    resource_class = WebResource


class RedesSocialesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('facebook','twitter','instagram','estado','fecha_creacion')
    search_fields = ['facebook']
    resource_class = RedesSocialesResource

class ContactoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('nombre','apellidos','correo','asunto','mensaje','estado','fecha_creacion')
    search_fields = ['correo']
    resource_class = ContactoResource

class SuscriptorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('correo','estado','fecha_creacion')
    search_fields = ['correo']
    resource_class = SuscriptorResource

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Web,WebAdmin)
admin.site.register(RedesSociales,RedesSocialesAdmin)
admin.site.register(Contacto,ContactoAdmin)
admin.site.register(Suscriptor,SuscriptorAdmin)
