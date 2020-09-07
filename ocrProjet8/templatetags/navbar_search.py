from django import template

from search.forms import SearchForm

register = template.Library()


class NavbarSearchNode(template.Node):
    def __init__(self):
        self.form = SearchForm()

    def render(self, context):
        self.rmedia()
        return self.form

    def rmedia(self):
        return self.form.media


@register.tag(name='navbar_search')
def navbar_search(parser, token):
    return NavbarSearchNode()



