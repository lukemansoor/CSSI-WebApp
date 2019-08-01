#main.py
#the import section
import webapp2
import jinja2
import io
import os
'''from google.cloud import vision
from google.cloud.vision import types'''

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
searchquery="Burger"


class RecipeFinder(webapp2.RequestHandler):
    def get(self):
        recipe_id_endpoint_url='https://api.spoonacular.com/recipes/search?query={}&number=1&apiKey=97d098f7ed6849a5bf2377f5bc2cbfbf'.format(searchquery)
        recipe_id_response=urlfetch.fetch(recipe_id_endpoint_url).content
        recipe_id_as_json=json.loads(recipe_id_response)
        id_result=recipe_id_as_json['results'][0]
        recipe_id=id_result['id']

        #the variable recipe_id is the id that should be passed onto the endpoint url to recieve data for the ingredients and such 
        ingredient_endpoint_url='https://api.spoonacular.com/recipes/{}/ingredientWidget.json?apiKey=97d098f7ed6849a5bf2377f5bc2cbfbf'.format(recipe_id)
        ingredient_response=urlfetch.fetch(ingredient_endpoint_url).content
        ingredient_as_json=json.loads(ingredient_response)
        #this following for loop is used to make sure the api request returns the necessary values 
        for i in ingredient_as_json['ingredients']:
            self.response.headers['Content-Type'] = 'text/html'
            self.response.write(i['name'] + " " + str(i['amount']['metric']['value']) + i['amount']['metric']['unit'])
            self.response.write("<br />\n")

        recipe_endpoint_url='https://api.spoonacular.com/recipes/{}/analyzedInstructions?apiKey=97d098f7ed6849a5bf2377f5bc2cbfbf'.format(recipe_id)
        recipe_response=urlfetch.fetch(recipe_endpoint_url).content
        recipe_as_json=json.loads(recipe_response)
        test= recipe_as_json[0]['steps']
        for i in test:
            self.response.headers['Content-Type'] = 'text/html'
            self.response.write(i['step'])
            self.response.write("<br />\n")


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
    ('/recipe', RecipeFinder),
    ], debug=True)
