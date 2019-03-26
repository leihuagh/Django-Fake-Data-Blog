from django.shortcuts import render, redirect
from .forms import ContactForm


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    form = ContactForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        print(form.cleaned_data.get('fullname'))
        print(form.cleaned_data.get('email'))
        print(form.cleaned_data.get('content'))
        form = ContactForm()
        return redirect('/contact')
    # if request.method == 'POST':
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, 'contact.html', context)
