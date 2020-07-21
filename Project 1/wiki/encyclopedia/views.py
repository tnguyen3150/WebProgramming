#import markdown as md
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
	contents=util.get_entry(title)
	return render(request, "encyclopedia/contents.html", {
		"contents":md.markdown(contents)			
	})
