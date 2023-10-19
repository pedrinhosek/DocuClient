
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, FormView, DetailView, DeleteView
from django.urls import reverse_lazy




from PyPDF2 import PdfReader
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image




import tempfile
from django.http import HttpResponse
from django.template import loader

from django.http import HttpResponse

from django.template import loader
import weasyprint


class ContratoCreate(UserPassesTestMixin, FormView):
    form_class = ContratoCreateForm
    template_name = '02_contrato/create.html'

    def get_success_url(self):
        url = reverse('contrato_create', args=[self.kwargs.get('pk_pessoa')])
        return url

    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
            pessoa=Pessoa.objects.filter(id=self.kwargs.get('pk_pessoa')).first(),
            BASE_PATH=self.request.META['HTTP_HOST'] + settings.STATIC_URL[:len(settings.STATIC_URL) - 1]
        )

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        files = form.cleaned_data["images"]
        pessoa = Pessoa.objects.filter(id=self.kwargs.get('pk_pessoa')).first()

        for documento in files:
            pdf = PyPDF2.PdfReader(documento)
            temp_dir = tempfile.TemporaryDirectory()

            temp_file_path = f"{temp_dir.name}/temp.pdf"
            with open(temp_file_path, 'wb') as temp_file:
                for chunk in documento.chunks():
                    temp_file.write(chunk)

            for page_number in range(len(pdf.pages)):
                images = convert_from_path(temp_file_path, first_page=page_number + 1, last_page=page_number + 1, output_folder=temp_dir.name)

                if images:
                    image = images[0]
                    image_path = f"{temp_dir.name}/page_{page_number + 1}.jpg"
                    image.save(image_path, 'JPEG')

                    # Criar um objeto InMemoryUploadedFile a partir da imagem
                    with open(image_path, 'rb') as img_file:
                        img_data = img_file.read()
                        img_file = InMemoryUploadedFile(
                            file=io.BytesIO(img_data),
                            field_name=None,
                            name=image_path.split("/")[-1],
                            content_type="image/jpeg",
                            size=len(img_data),
                            charset=None
                        )

                        doc_contrato = DocumentoContrato(
                            cliente=pessoa,
                            documento=img_file
                        )
                        doc_contrato.save()

        pessoa.doc_inserido = True
        pessoa.save()

        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        return True


class DeleteDocContrato(UserPassesTestMixin, DeleteView):
    model = DocumentoContrato
    template_name = '02_contrato/delete_doc.html'
    pk_url_kwarg = 'pk_doc'

    def get_success_url(self):
        url = reverse('contrato_create', args=[self.kwargs.get('pk_pessoa')])
        return url

    def test_func(self):
        return True


class PrintContrato(UserPassesTestMixin, DetailView):
    model = Pessoa
    pk_url_kwarg = 'pk_pessoa'
    template_name = '02_contrato/print.html'

    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
        )

    def test_func(self):
        return True




# def html_to_pdf(request):
#     # Renderize a página HTML usando um template do Django
#     template = loader.get_template('sua_template.html')
#     context = {}  # Inclua dados contextuais, se necessário
#     rendered_html = template.render(context)
#
#     # Use o WeasyPrint para converter o HTML em PDF
#     pdf_file = weasyprint.HTML(string=rendered_html).write_pdf()
#
#     # Responda com o PDF gerado
#     response = HttpResponse(pdf_file, content_type='application/pdf')
#     response['Content-Disposition'] = 'inline; filename="output.pdf"'  # Nome do arquivo a ser exibido no navegador
#     return response


class PDFContrato(View):
    # model = Pessoa
    # pk_url_kwarg = 'pk_pessoa'
    template_name = '02_contrato/print.html'  # Substitua pelo nome do seu template

    def get(self, request, *args, **kwargs):
        # Renderize a página HTML usando um template do Django
        template = loader.get_template(self.template_name)
        context = {}  # Inclua dados contextuais, se necessário
        rendered_html = template.render(context)

        # Use o WeasyPrint para converter o HTML em PDF
        pdf_file = weasyprint.HTML(string=rendered_html).write_pdf()

        # Responda com o PDF gerado
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="output.pdf"'  # Nome do arquivo a ser exibido no navegador
        return response
