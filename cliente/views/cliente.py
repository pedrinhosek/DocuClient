from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from cliente.models import Pessoa
from cliente.forms import PessoaForm


class ClienteList(UserPassesTestMixin, ListView):
    model = Pessoa
    template_name = '01_cliente/list.html'

    def get_queryset(self):
        filtro = self.request.GET.get('filtro')
        if filtro == 'enviado':
            qs = Pessoa.objects.filter(contrato_enviado=True)
        elif filtro == 'nao_enviado':
            qs = Pessoa.objects.filter(contrato_enviado=False)
        elif filtro == 'todos':
            qs = Pessoa.objects.all()
        else:
            qs = Pessoa.objects.filter(contrato_enviado=False)
        return qs

    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
            cliente=True
        )

    def test_func(self):
        return True


class ClienteCreate(UserPassesTestMixin, CreateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = '01_cliente/create.html'
    success_url = reverse_lazy('cliente_list')

    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
            contrato=True
        )

    def test_func(self):
        return True


class ClienteUpdate(UserPassesTestMixin, UpdateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = '01_cliente/update.html'
    success_url = reverse_lazy('cliente_list')

    def get_context_data(self, **kwargs):
        return dict(
            super().get_context_data(**kwargs),
            contrato=True
        )

    def test_func(self):
        return True
