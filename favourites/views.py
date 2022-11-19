from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, RedirectView

from favourites.forms import AddFavouritesForm, DeleteFavouritesForm
from favourites.mixins import GetFavouritesMixin


class FavouritesView(LoginRequiredMixin, GetFavouritesMixin, TemplateView):
    template_name = 'favourites/product_favourite.html'

    def get_context_data(self, **kwargs):
        context = super(FavouritesView, self).get_context_data()
        context.update({
            'favourites': self.get_favourites_object()
        })
        return context


class AddFavouritesView(GetFavouritesMixin, RedirectView):
    url = reverse_lazy('favourites')

    def post(self, request, *args, **kwargs):
        form = AddFavouritesForm(request.POST,
                                 favourites=self.get_favourites_object())
        if form.is_valid():
            messages.success(request, message='Product was successfully added to favourites!') # noqa
            form.save()
        return self.get(request, *args, **kwargs)


class DeleteFavouritesView(GetFavouritesMixin, RedirectView):
    url = reverse_lazy('favourites')

    def post(self, request, *args, **kwargs):
        form = DeleteFavouritesForm(request.POST,
                                    favourites=self.get_favourites_object())
        if form.is_valid():
            messages.warning(request, message='Product was successfully deleted!') # noqa
            form.save()
        return self.get(request, *args, **kwargs)
