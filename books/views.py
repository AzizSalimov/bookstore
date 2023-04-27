from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Order, Books
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import JsonResponse
from django.views import View
from django.http import HttpResponse, Http404

import json


class BooksListView(ListView):
    model = Book
    template_name = 'list.html'


class BooksDetailView(DetailView):
    model = Book
    template_name = 'detail.html'


class SearchResultsListView(ListView):
    model = Book
    template_name = 'search_result.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )


class BookCheckoutView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'checkout.html'
    login_url = 'login'


def paymentComplete(request):
    body = json.loads(request.body)
    print('BODY:', body)
    product = Book.objects.get(id=body['productId'])
    Order.objects.create(
        product=product
    )
    return JsonResponse('Payment completed!', safe=False)


def quentuty_list(request):
    quentities = Books.objects.all()
    return render(request, 'detail.html', {'questities': quentities})


def custom_404(request, exceotion):
    return HttpResponse('Xatolok!', status=404)
# class MyProfile(LoginRequiredMixin, View):
#     def get(self, request):
#         user_form = UserUpdateForm(instance=request.user)
#         profile_form = ProfileUpdateForm(instance=request.user.profile)
#
#         context = {
#             'user_form': user_form,
#             'profile_form': profile_form
#         }
#
#         return render(request, 'users/profile.html', context)
#
#     def post(self, request):
#         user_form = UserUpdateForm(
#             request.POST,
#             instance=request.user
#         )
#         profile_form = ProfileUpdateForm(
#             request.POST,
#             request.FILES,
#             instance=request.user.profile
#         )
#
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#
#             messages.success(request, 'Your profile has been updated successfully')
#
#             return redirect('profile')
#         else:
#             context = {
#                 'user_form': user_form,
#                 'profile_form': profile_form
#             }
#             messages.error(request, 'Error updating you profile')
#
#             return render(request, 'users/profile.html', context)
#
