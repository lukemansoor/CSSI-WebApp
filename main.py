#main.py
# the import section
import webapp2

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('Hello, World!') #the response

class SecretPage(webapp2.RequestHandler):
    def get(self): #get requests
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h1 style ="background-color: blue;">This is my secret page</h1>')


# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the Main Page Handler
], debug=True)
