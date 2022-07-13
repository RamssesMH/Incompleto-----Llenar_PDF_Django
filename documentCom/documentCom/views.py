from django.shortcuts import render, redirect
from django.template import Template, Context
from django.shortcuts import render, redirect
import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

def index(request):
    t = 'index.html'



    if request.method == "POST":

        usuariop = request.POST["usuario"]
        nombrep = request.POST["nombre"]
        matriculap = request.POST["matricula"]
        RFCp = request.POST["rfc"]

        try:
            template = get_template("plantillas/doc.html")
            context = {'usuario': usuariop, 'nombre': nombrep, 'matricula': matriculap, 'rfc': RFCp}
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            # create a pdf
            pisa_status = pisa.CreatePDF(
            html, dest=response)
            # if error then show some funny view
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response
        except:
            pass
        HttpResponseRedirect("formulario/")

        
    return render(request, t)