from marshmallow import Schema, EXCLUDE


class BaseSchema(Schema):

    class Meta:
        unknown = EXCLUDE
    
    load_breaks = []

    def load(self, *args, **kwargs):
        json_args = args[0]

        for i, to_break in enumerate(self.load_breaks):
            data = {}

            for field in filter(lambda f: f in json_args, to_break['load_from']):
                data[field] = json_args.pop(field)

            self.load_breaks[i]['data'] = data

        model_obj = super().load(*args, *kwargs)

        for to_break in self.load_breaks:
            child_model_obj = to_break['dataclass'].Schema().load(to_break['data'])
            setattr(model_obj, to_break['property'], child_model_obj)
        
        return model_obj
    
    def dump(self, *args, **kwargs):
        _partial = super().dump(*args, **kwargs)

        if isinstance(_partial, list):
            for i, data in enumerate(_partial):
                _partial[i] = self._dump(data)

            return _partial
        
        return self._dump(_partial)
    
    def _dump(self, _partial):
        for n, field in self._declared_fields.items():
            formated_name = n
            index = n if not field.data_key else field.data_key

            _partial[formated_name] = _partial[index]

            if formated_name != index:
                _partial.pop(index)

        return _partial
