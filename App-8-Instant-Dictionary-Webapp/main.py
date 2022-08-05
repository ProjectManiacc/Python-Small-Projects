import inspect

import justpy as jp
from Webapp.home import Home
from Webapp.about import About
from Webapp.dictionary import Dictionary
from Webapp import page

imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(obj.path, obj.serve)

jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)
jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy()
