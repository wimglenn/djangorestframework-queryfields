Django REST framework QueryFields
=================================

|gh| |codecov| |pypi| |womm|

.. |gh| image:: https://github.com/wimglenn/djangorestframework-queryfields/actions/workflows/main.yml/badge.svg
.. _gh: https://github.com/wimglenn/djangorestframework-queryfields/actions

.. |codecov| image:: https://codecov.io/gh/wimglenn/djangorestframework-queryfields/branch/main/graph/badge.svg?token=WeqbZ83YRg
.. _codecov: https://codecov.io/gh/wimglenn/djangorestframework-queryfields

.. |pypi| image:: https://img.shields.io/pypi/v/djangorestframework-queryfields.svg
.. _pypi: https://pypi.org/project/djangorestframework-queryfields

.. |womm| image:: https://cdn.rawgit.com/nikku/works-on-my-machine/v0.2.0/badge.svg
.. _womm: https://github.com/nikku/works-on-my-machine

Allows clients to control which fields will be sent in the API response.  Fields are specified in the query, e.g.

.. code-block:: 

    # You want a list of users but you're only interested in the fields "id" and "username":
    
    GET /users/?fields=id,username
    
    [
      {
        "id": 1,
        "username": "tom"
      },
      {
        "id": 2,
        "username": "wim"
      }
    ]

    
    # You want to see every field except "id" for the specific user wim:
    
    GET /users/2/?fields!=id
    
    {
      "username": "wim",
      "email": "hey@wimglenn.com",
      "spirit_animal": "raccoon"
    }

**Supported Django versions**: 1.7 - 3.2+.  Check the `CI matrix <https://github.com/wimglenn/djangorestframework-queryfields/blob/main/.github/workflows/main.yml/>`_ for details.

Documentation is hosted on `Read The Docs <http://djangorestframework-queryfields.readthedocs.io/>`_.

Developers, developers, developers!
-----------------------------------

Want to contribute to the project? This is how to run the test suite:

.. code-block:: bash

   # get the codez
   git clone https://github.com/wimglenn/djangorestframework-queryfields.git

   # create and/or activate your virtualenv, this or something like it:
   cd djangorestframework-queryfields
   python3 -m venv .venv
   source .venv/bin/activate

   # installing the app in your venv
   pip install --editable ".[dev]"
   git checkout -b myfeature

   # hack away, then ...
   pytest
