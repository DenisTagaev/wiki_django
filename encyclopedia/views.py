from django.shortcuts import render, redirect

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "title": 'Encyclopedia'
    })

def entry(request, entry):
    entry = util.get_entry(entry)
    req_title = request.path_info.strip('/').split('/')[-1]

    if not entry:
        return redirect('/error')

    return render(request, "encyclopedia/entry.html", {
        "entry": entry,
        "title": req_title
    })

def non_existent_entry(request):
    return render(request, "encyclopedia/404.html", {
        "title": 'Error'
    })
