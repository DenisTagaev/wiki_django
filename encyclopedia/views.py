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
