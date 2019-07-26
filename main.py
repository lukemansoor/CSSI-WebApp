#main.py
# the import section
import webapp2
import jinja2
import os

# this initializes the jinja2 environment
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(_file)),
    extensions=['jinja.ext.autoescape'],
    autoescape=True)

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('Hello, World!') #the response

class SecretPage(webapp2.RequestHandler):
    def get(self): #get requests
        welcome_template = the_jinja_env.get_template(templates/'welcome.html')
        self.response.write(welcome_template.render())

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the Main Page Handler
    ('/secret', SecretPage),
    ], debug=True)
