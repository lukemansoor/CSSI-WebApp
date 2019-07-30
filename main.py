#main.py
#the import section
import webapp2
import jinja2
import io
import os
from google.cloud import vision
from google.cloud.vision import types

# this initializes the jinja2 environment
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

'''class run_quickstart(webapp2.RequestHandler):
    def get(self):
        # Instantiates a client
        # [START vision_python_migration_client]
        client = vision.ImageAnnotatorClient()
        # [END vision_python_migration_client]

        # The name of the image file to annotate
        file_name = os.path.join(
            os.path.dirname(__file__),
            '/phonepicutres-TA.jpg')

        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations


        print('Labels:')
        for label in labels:
            print(label.description)
        # [END vision_quickstart]
'''

class RecipeFinder(webapp2.RequestHandler):
    def get(self):
        endpoint_url='https://api.spoonacular.com/recipes/search?query=' + searchquery + '?apiKey=97d098f7ed6849a5bf2377f5bc2cbfbf'
        
    
# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('Hello, World!') #the response

class SecretPage(webapp2.RequestHandler):
    def get(self): #get requests
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the Main Page Handler
    ('/secret', SecretPage),
    ], debug=True)
