Usage
-----

.. code-block:: bash

    GET http://127.0.0.1:8000/things/

    HTTP/1.1 200 OK
    ...
    [
      {
        "id": 1,
        "key1": "val1",
        "key2": "val2",
        "key3": "val3",
      },
      {
        "id": 2,
        "key1": "valA",
        "key2": "valB",
        "key3": "valC",
      }
    ]


    GET http://127.0.0.1:8000/things/?fields=id,key2

    HTTP/1.1 200 OK
    ...
    [
      {
        "id": 1,
        "key2": "val2",
      },
      {
        "id": 2,
        "key2": "valB",
      }
    ]


    GET http://127.0.0.1:8000/things/?fields!=key2

    HTTP/1.1 200 OK
    ...
    [
      {
        "id": 1,
        "key1": "val1",
        "key3": "val3",
      },
      {
        "id": 2,
        "key1": "valA",
        "key3": "valC",
      }
    ]


