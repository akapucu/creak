
from baseplugin import BasePlugin

class Plugin(BasePlugin):

    def init_plugin(self):
        self.required_params['name'] = True

    def run(self, kwargs):
        print("Hello %s" % kwargs['name'])
