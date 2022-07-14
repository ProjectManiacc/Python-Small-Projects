import justpy as jp
from Webapp import layout
from Webapp import page

class About(page.Page):

    path = '/about'
    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text='This is the About page!', classes='text-4xl m-2')
        jp.Div(a=div, text = """ Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem
         Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum 
         Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum 
         Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum 
         Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum 
         Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum 
         Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum 
         Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum 
         Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum 
         Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum Lorem Impsum  
          """, classes='text-lg')
        return wp

