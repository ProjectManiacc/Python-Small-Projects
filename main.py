import justpy as jp
from Webapp.home import Home
from Webapp.about import About
jp.Route(Home.path,Home.serve)
jp.Route(About.path,About.serve)

jp.justpy()