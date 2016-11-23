Django REST framework QueryFields documentation
===============================================

Allows clients to control which fields will be sent in the API response.  The idea is based on a recipe described in the official documentation, `Dynamically modifying fields <http://www.django-rest-framework.org/api-guide/serializers/#dynamically-modifying-fields>`_, adapted to allow API users to specify fields via GET request query parameters.  

Doing the filtering server-side instead of client-side can have advantages:

- Fewer bytes down the wire = snappier ajax for your webapps
- Less backend server load if expensive-to-serialize fields go unneeded
- For thin clients; a better choice if client-side is a dumb/low-power device


Contents
--------

.. toctree::
   :maxdepth: 2

   installation
   quickstart
   usage
   faq
