from flask import jsonify

errors = {
    'UserAlreadyExistsError': {
        'message': "A user with that username already exists.",
        'status': 409,
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },
    'FieldDoesNotExist': {
        "message": "A ORM ( Mongoengine ) field mismatch",
        'status': 422,
    },
    'ExpiredSignatureError': {
        'status': 401,
        "message": "A refresh token is expired"
    },
    'DuplicateKeyError': {
        'status': 400,
        "message": "Your input data is Duplicated"
    },
    "NotUniqueError": {
        'status': 400,
        "message": "Your input data is Duplicated"
    },
    "DecodeError": {
        'status': 401,
        "message": "jwt DecodeError"
    },
}