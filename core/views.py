from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Produto


class IndexView(ListView):
    models = Produto
    template_name = 'index.html'
    # tras todos produtos
    queryset = Produto.objects.all()
    # recupera os dados do template
    context_object_name = 'produtos'


class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')  # atualizou manda para o index


class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')


class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'produto_del.html'
    success_url = reverse_lazy('index')
