# coding: utf-8

"""
    spoonacular API

    The spoonacular Nutrition, Recipe, and Food API allows you to access over 380,000 recipes, thousands of ingredients, 80,000 food products, and 100,000 menu items. Our food ontology and semantic recipe search engine makes it possible to search for recipes using natural language queries, such as \"gluten free brownies without sugar\" or \"low fat vegan cupcakes.\" You can automatically calculate the nutritional information for any recipe, analyze recipe costs, visualize ingredient lists, find recipes for what's in your fridge, find recipes based on special diets, nutritional requirements, or favorite ingredients, classify recipes into types and cuisines, convert ingredient amounts, or even compute an entire meal plan. With our powerful API, you can create many kinds of food and especially nutrition apps.  Special diets/dietary requirements currently available include: vegan, vegetarian, pescetarian, gluten free, grain free, dairy free, high protein, whole 30, low sodium, low carb, Paleo, ketogenic, FODMAP, and Primal.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: david@spoonacular.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InlineObject3(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'title': 'str',
        'image': 'file',
        'ingredients': 'str',
        'instructions': 'str',
        'ready_in_minutes': 'float',
        'servings': 'float',
        'mask': 'str',
        'background_image': 'str',
        'author': 'str',
        'background_color': 'str',
        'font_color': 'str',
        'source': 'str'
    }

    attribute_map = {
        'title': 'title',
        'image': 'image',
        'ingredients': 'ingredients',
        'instructions': 'instructions',
        'ready_in_minutes': 'readyInMinutes',
        'servings': 'servings',
        'mask': 'mask',
        'background_image': 'backgroundImage',
        'author': 'author',
        'background_color': 'backgroundColor',
        'font_color': 'fontColor',
        'source': 'source'
    }

    def __init__(self, title=None, image=None, ingredients=None, instructions=None, ready_in_minutes=None, servings=None, mask=None, background_image=None, author=None, background_color=None, font_color=None, source=None):  # noqa: E501
        """InlineObject3 - a model defined in OpenAPI"""  # noqa: E501

        self._title = None
        self._image = None
        self._ingredients = None
        self._instructions = None
        self._ready_in_minutes = None
        self._servings = None
        self._mask = None
        self._background_image = None
        self._author = None
        self._background_color = None
        self._font_color = None
        self._source = None
        self.discriminator = None

        self.title = title
        self.image = image
        self.ingredients = ingredients
        self.instructions = instructions
        self.ready_in_minutes = ready_in_minutes
        self.servings = servings
        self.mask = mask
        self.background_image = background_image
        if author is not None:
            self.author = author
        if background_color is not None:
            self.background_color = background_color
        if font_color is not None:
            self.font_color = font_color
        if source is not None:
            self.source = source

    @property
    def title(self):
        """Gets the title of this InlineObject3.  # noqa: E501

        The title of the recipe.  # noqa: E501

        :return: The title of this InlineObject3.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InlineObject3.

        The title of the recipe.  # noqa: E501

        :param title: The title of this InlineObject3.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def image(self):
        """Gets the image of this InlineObject3.  # noqa: E501

        The binary image of the recipe as jpg.  # noqa: E501

        :return: The image of this InlineObject3.  # noqa: E501
        :rtype: file
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this InlineObject3.

        The binary image of the recipe as jpg.  # noqa: E501

        :param image: The image of this InlineObject3.  # noqa: E501
        :type: file
        """
        if image is None:
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image

    @property
    def ingredients(self):
        """Gets the ingredients of this InlineObject3.  # noqa: E501

        The ingredient list of the recipe, one ingredient per line (separate lines with \\n).  # noqa: E501

        :return: The ingredients of this InlineObject3.  # noqa: E501
        :rtype: str
        """
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients):
        """Sets the ingredients of this InlineObject3.

        The ingredient list of the recipe, one ingredient per line (separate lines with \\n).  # noqa: E501

        :param ingredients: The ingredients of this InlineObject3.  # noqa: E501
        :type: str
        """
        if ingredients is None:
            raise ValueError("Invalid value for `ingredients`, must not be `None`")  # noqa: E501

        self._ingredients = ingredients

    @property
    def instructions(self):
        """Gets the instructions of this InlineObject3.  # noqa: E501

        The instructions to make the recipe. One step per line (separate lines with \\n).  # noqa: E501

        :return: The instructions of this InlineObject3.  # noqa: E501
        :rtype: str
        """
        return self._instructions

    @instructions.setter
    def instructions(self, instructions):
        """Sets the instructions of this InlineObject3.

        The instructions to make the recipe. One step per line (separate lines with \\n).  # noqa: E501

        :param instructions: The instructions of this InlineObject3.  # noqa: E501
        :type: str
        """
        if instructions is None:
            raise ValueError("Invalid value for `instructions`, must not be `None`")  # noqa: E501

        self._instructions = instructions

    @property
    def ready_in_minutes(self):
        """Gets the ready_in_minutes of this InlineObject3.  # noqa: E501

        The number of minutes it takes to get the recipe on the table.  # noqa: E501

        :return: The ready_in_minutes of this InlineObject3.  # noqa: E501
        :rtype: float
        """
        return self._ready_in_minutes

    @ready_in_minutes.setter
    def ready_in_minutes(self, ready_in_minutes):
        """Sets the ready_in_minutes of this InlineObject3.

        The number of minutes it takes to get the recipe on the table.  # noqa: E501

        :param ready_in_minutes: The ready_in_minutes of this InlineObject3.  # noqa: E501
        :type: float
        """
        if ready_in_minutes is None:
            raise ValueError("Invalid value for `ready_in_minutes`, must not be `None`")  # noqa: E501

        self._ready_in_minutes = ready_in_minutes

    @property
    def servings(self):
        """Gets the servings of this InlineObject3.  # noqa: E501

        The number of servings that you can make from the ingredients.  # noqa: E501

        :return: The servings of this InlineObject3.  # noqa: E501
        :rtype: float
        """
        return self._servings

    @servings.setter
    def servings(self, servings):
        """Sets the servings of this InlineObject3.

        The number of servings that you can make from the ingredients.  # noqa: E501

        :param servings: The servings of this InlineObject3.  # noqa: E501
        :type: float
        """
        if servings is None:
            raise ValueError("Invalid value for `servings`, must not be `None`")  # noqa: E501

        self._servings = servings

    @property
    def mask(self):
        """Gets the mask of this InlineObject3.  # noqa: E501

        The mask to put over the recipe image (\"ellipseMask\", \"diamondMask\", \"diamondMask\", \"starMask\", \"heartMask\", \"potMask\", \"fishMask\").  # noqa: E501

        :return: The mask of this InlineObject3.  # noqa: E501
        :rtype: str
        """
        return self._mask

    @mask.setter
    def mask(self, mask):
        """Sets the mask of this InlineObject3.

        The mask to put over the recipe image (\"ellipseMask\", \"diamondMask\", \"diamondMask\", \"starMask\", \"heartMask\", \"potMask\", \"fishMask\").  # noqa: E501

        :param mask: The mask of this InlineObject3.  # noqa: E501
        :type: str
        """
        if mask is None:
            raise ValueError("Invalid value for `mask`, must not be `None`")  # noqa: E501

        self._mask = mask

    @property
    def background_image(self):
        """Gets the background_image of this InlineObject3.  # noqa: E501

        The background image (\"none\",\"background1\", or \"background2\").  # noqa: E501

        :return: The background_image of this InlineObject3.  # noqa: E501
        :rtype: str
        """
        return self._background_image

    @background_image.setter
    def background_image(self, background_image):
        """Sets the background_image of this InlineObject3.

        The background image (\"none\",\"background1\", or \"background2\").  # noqa: E501

        :param background_image: The background_image of this InlineObject3.  # noqa: E501
        :type: str
        """
        if background_image is None:
            raise ValueError("Invalid value for `background_image`, must not be `None`")  # noqa: E501

        self._background_image = background_image

    @property
    def author(self):
        """Gets the author of this InlineObject3.  # noqa: E501

        The author of the recipe.  # noqa: E501

        :return: The author of this InlineObject3.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this InlineObject3.

        The author of the recipe.  # noqa: E501

        :param author: The author of this InlineObject3.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def background_color(self):
        """Gets the background_color of this InlineObject3.  # noqa: E501

        The background color on the recipe card as a hex-string.  # noqa: E501

        :return: The background_color of this InlineObject3.  # noqa: E501
        :rtype: str
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this InlineObject3.

        The background color on the recipe card as a hex-string.  # noqa: E501

        :param background_color: The background_color of this InlineObject3.  # noqa: E501
        :type: str
        """

        self._background_color = background_color

    @property
    def font_color(self):
        """Gets the font_color of this InlineObject3.  # noqa: E501

        The font color on the recipe card as a hex-string.  # noqa: E501

        :return: The font_color of this InlineObject3.  # noqa: E501
        :rtype: str
        """
        return self._font_color

    @font_color.setter
    def font_color(self, font_color):
        """Sets the font_color of this InlineObject3.

        The font color on the recipe card as a hex-string.  # noqa: E501

        :param font_color: The font_color of this InlineObject3.  # noqa: E501
        :type: str
        """

        self._font_color = font_color

    @property
    def source(self):
        """Gets the source of this InlineObject3.  # noqa: E501

        The source of the recipe.  # noqa: E501

        :return: The source of this InlineObject3.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this InlineObject3.

        The source of the recipe.  # noqa: E501

        :param source: The source of this InlineObject3.  # noqa: E501
        :type: str
        """

        self._source = source

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineObject3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
