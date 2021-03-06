from django.views.generic import TemplateView
from django.shortcuts import render


class HomeView(TemplateView):
    title = ''
    template = 'pages/home.html'
    component = 'HomePage.js'

    def get(self, request):
        # gets passed to react via window.props
        props = {
            'users': [
                {'username': 'alice'},
                {'username': 'bob'},
            ]
        }

        context = {
            'title': self.title,
            'component': self.component,
            'props': props,
        }

        return render(request, self.template, context)




