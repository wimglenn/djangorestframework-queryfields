from rest_framework import serializers


class Kapow(Exception):
    pass


class BoomField(serializers.CharField):

    def to_representation(self, value):
        raise Kapow
