# Guardar imagen en Django Python 🐍

##### 1. Configurar tu settings.py

`

    import os
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

`

#### 2. Configurar tu archivo urls.py del proyecto

`

    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
    	# tus urls
    ]

    if settings.DEBUG:
    	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    	`

#### 3. Definiendo tu models.py

`

    from django.db import models

    class Documento(models.Model):
    	descripcion = models.CharField(max_length=255, blank=True)
    	documento = models.FileField(upload_to='documentos/')
    	subido_a = models.DateTimeField(auto_now_add=True)

`

#### 4. Definiendo tu forms.py

`

    from django import forms
    import *.models

    class DocumentoForm(forms.ModelForm):
    	class Meta:
    		model = Documento
    		fields = ('descripcion', 'documento', )

`

#### 5. Define tu views.py

`

    def mi_metodo(request):
    	if request.method == 'POST':
    		form = DocumentoForm(request.POST, request.FILES)
    		if form.is_valid():
    			form.save()
    			return redirect('index')#redirigue a donde deseas
    	else:
    		form = DocumentoForm()
    	return render(request, 'mi_template.html', {
    		'form': form
    	})
    `

#### 6 Pintando el formulario en tu plantilla index.html

`

    <form method="post" enctype="multipart/form-data">
    	{% csrf_token %}
    	{{ form.as_p }}
    	<button type="submit">Subir</button>
      </form>

`

![](https://pandao.github.io/editor.md/images/logos/editormd-logo-180x180.png)
