import random
from django.shortcuts import render, redirect
from markdown2 import Markdown
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "title": 'Encyclopedia'
    })

def index_search(request):
    query = request.POST.get('q')
    autofocus = True

    if query:
        if util.get_entry(query):
            return entry(request, query)

        # Filter entries where the name includes the query
        filtered_entries = [ent for ent in util.list_entries() if query.lower() in ent.lower()]
    else:
        # If no query provided, return all entries
        filtered_entries = util.list_entries()

    return render(request, "encyclopedia/index.html", {
        "entries": filtered_entries,
        "title": 'Encyclopedia',
        "autofocus": autofocus
    })

def entry(request, entry):
    entry = util.get_entry(entry)
    markdowner = Markdown(extras=["break-on-newline"])
    req_title = request.path_info.strip('/').split('/')[-1]

    if not entry:
        return redirect('/error')

    return render(request, "encyclopedia/entry.html", {
        "entry": markdowner.convert(entry),
        "title": req_title
    })

def edit_entry(request, entry_title):
    entry = util.get_entry(entry_title)

    if not entry:
        return redirect('/error')

    if request.method == 'GET':
        return render(request, "encyclopedia/edit_entry.html", {
            "entry": entry,
            "title": entry_title
        })

    if request.method == 'POST':
        content = "\n".join(line.strip() for line in request.POST["content"].split("\n"))
        util.save_entry(entry_title, content)
        return redirect(f'/wiki/{entry_title}')

def random_entry(request):
    selected_entry = random.choice(util.list_entries())
    return redirect(f'/wiki/{selected_entry}')

def new_entry(request):
    if request.method == 'GET':
        return render(request, "encyclopedia/new_entry.html", {
            "title": 'New Entry'
        })

    if request.method == 'POST':
        title = request.POST["title"]
        content = request.POST["content"]

        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/new_entry.html", {
                "title": 'New Entry',
                "error_message": 'Article with this title already exists'
            })

        util.save_entry(title, content)
        return redirect(f'/wiki/{title}')

def non_existent_entry(request):
    return render(request, "encyclopedia/404.html", {
        "title": 'Error'
    })
