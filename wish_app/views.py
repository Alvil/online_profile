from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from .models import Wish


class WishList(generic.ListView):
    model = Wish
    template_name = 'wish_app/index.html'


class CreateWish(generic.CreateView):
    model = Wish
    fields = ('wisher', 'wish')
    template_name = 'wish_app/create_wish.html'
    success_url = reverse_lazy('wish:wishlist')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        wish_object = Wish.objects.filter(wish_check__iexact=self.object.wish.lower())
        if wish_object:
            wish_object = wish_object[0]
            wish_object.instances += 1
            wish_object.save()
            return HttpResponseRedirect (reverse_lazy('wish:wishlist'))
        else:
            self.object.save()
            return super(CreateWish, self).form_valid(form)
