import six

class QueryFieldsMixin(object):

    # If using Django filters in the API, these labels mustn't conflict with any model field names.
    include_arg_name = 'fields'
    exclude_arg_name = 'fields!'

    # Split field names by this string.  It doesn't necessarily have to be a single character.
    # Avoid RFC 1738 reserved characters i.e. ';', '/', '?', ':', '@', '=' and '&'
    delimiter = ','

    def __init__(self, *args, **kwargs):
        super(QueryFieldsMixin, self).__init__(*args, **kwargs)

        try:
            if not self.context:
                return
            request = self.context.get('request')
            if not request:
                return
            method = request.method
            if method != 'GET':
                return
        except (AttributeError, TypeError, KeyError):
            # The serializer was not initialized with request context.
            return
        try:
            query_params = request.query_params
        except AttributeError:
            # DRF 2
            query_params = getattr(request, 'QUERY_PARAMS', request.GET)

        includes = query_params.getlist(self.include_arg_name)
        include_field_names = {name for names in includes for name in names.split(self.delimiter) if name}

        excludes = query_params.getlist(self.exclude_arg_name)
        exclude_field_names = {name for names in excludes for name in names.split(self.delimiter) if name}

        if not include_field_names and not exclude_field_names:
            # No user fields filtering was requested, we have nothing to do here.
            self._reset_context_for_sub_fields(self.fields)
            return

        serializer_field_names = set(self.fields)

        fields_to_drop = serializer_field_names & exclude_field_names
        if include_field_names:
            fields_to_drop |= serializer_field_names - include_field_names

        for field in fields_to_drop:
            self.fields.pop(field)

        self._reset_context_for_sub_fields(self.fields)

    def _reset_context_for_sub_fields(self, fields):
        for field in six.itervalues(fields.fields):
            if not field.context:
                # print 'resetting context for {}'.format(type(field))
                delattr(field, 'context')
                setattr(field, '_context', self.context)
                self._reset_context_for_sub_fields(field)
