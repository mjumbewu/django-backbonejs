from django import template
from django.conf import settings

register = template.Library()

SCRIPT_TAG = '<script src="%s%s.js" type="text/javascript"></script>'

class BackboneJSNode(template.Node):

    def __init__(self, args):
        self.args = set(args)

    def render_all_scripts(self):
        results = [
#            ... Other Backbone plugins ...
        ]
        return '\n'.join(results)

    def render(self, context):
        tags = [
            SCRIPT_TAG % (settings.STATIC_URL, 'underscore'),
            SCRIPT_TAG % (settings.STATIC_URL, 'backbone'),
        ]

        if 'all' in self.args:
            return tags + self.render_all_scripts()
        else:
            tags += [SCRIPT_TAG % (settings.STATIC_URL,tag) for tag in self.args]
            return '\n'.join(tags)

@register.tag(name='backbone_js')
def do_bootstrap_js(parser, token):
    print '\n'.join(token.split_contents())
    return BootstrapJSNode(token.split_contents()[1:])
