from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django import forms
from . import util
from markdown2 import Markdown
from random import randint

md = Markdown()


class NewEntryForm(forms.Form):
    title = forms.CharField(max_length=30, label="Title")
    md_content = forms.CharField(widget=forms.Textarea, label="", min_length=10)


class EditEntryForm(forms.Form):
    md_content = forms.CharField(widget=forms.Textarea, label="", min_length=10)


def entry_exists(title):
    for entry in util.list_entries():
        if title.lower() == entry.lower():
            return True
    return False


def index_redirect(request):
    return HttpResponseRedirect(reverse("encyclopedia:index"))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    raw_content = util.get_entry(title)
    if not raw_content:
        return HttpResponseNotFound('<h1>Entry does not exist.</h1> <a href="/">Go Home </a>')
    html_content = md.convert(raw_content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })


def edit(request, title):
    if request.method == "POST":
        form = EditEntryForm(request.POST)
        if form.is_valid():
            util.save_entry(title, form.cleaned_data["md_content"])
            return HttpResponseRedirect(reverse("encyclopedia:entry", args=(title,)))
        else:
            return render(request, "encyclopedia/edit.html", {
                "title": title,
                "message": "Content of the page must be at least 10 characters.",
                "form": form
            })
    raw_content = util.get_entry(title)
    if not raw_content:
        raise HttpResponseNotFound('<h1>Entry does not exist.</h1> <a href="/">Go Home </a>')
    edit_form = EditEntryForm(initial={"md_content":raw_content})
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "form": edit_form
    })


def search(request):
    query = request.GET.get("q")
    if util.get_entry(query):
        return HttpResponseRedirect(reverse("encyclopedia:entry", args=(query,)))
    matching_entries = []
    for entry in util.list_entries():
        if query.lower() in entry.lower():
            matching_entries.append(entry)

    return render(request, "encyclopedia/search.html", {
        "query": query,
        "entries": matching_entries
    })


def create(request):
    if request.method == "POST":
        create_form = NewEntryForm(request.POST)
        if create_form.is_valid():
            title = create_form.cleaned_data["title"].capitalize()
            md_content = create_form.cleaned_data["md_content"]
            if not entry_exists(title):
                util.save_entry(title, md_content)
                return HttpResponseRedirect(reverse("encyclopedia:entry", args=(title,)))
            else:
                return render(request, "encyclopedia/create.html", {
                    "message": f"The entry '{title}' already exists",
                    "form": create_form
                })
        else:
            return render(request, "encyclopedia/create.html", {
                "message": f"Form is not valid, check the fields",
                "form": create_form
            })
    create_form = NewEntryForm()
    return render(request, "encyclopedia/create.html", {
        "form": create_form
    })


def random(request):
    entries = util.list_entries()
    K = randint(0, len(entries)-1)
    return HttpResponseRedirect(reverse("encyclopedia:entry", args=(entries[K],)))