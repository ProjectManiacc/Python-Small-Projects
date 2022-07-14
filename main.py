import justpy as jp
from Webapp.home import Home
from Webapp.about import About
from Webapp.dictionary import Dictionary

jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)
jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy()
