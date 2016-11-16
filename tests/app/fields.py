from rest_framework import serializers


class Kapow(Exception):
    pass


class BoomField(serializers.CharField):

    # DRF 3
    def to_representation(self, value):
        raise Kapow

    # DRF 2
    def field_to_native(self, obj, field_name):
        raise Kapow
