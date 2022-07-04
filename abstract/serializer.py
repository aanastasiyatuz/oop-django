class BaseSerializer:
    class Meta:
        fields = []
        queryset = []

    def serialize_obj(self, obj):
        fields = self.Meta.fields
        representation = {}
        for field in fields:
            data = obj.__getattribute__(field)
            representation[field] = data
        return representation
    
    def serialize_queryset(self):
        queryset = self.Meta.queryset
        representation = []
        for obj in queryset:
            representation.append(self.serialize_obj(obj))
        return representation
    
    # @property
    # def data(self):
    #     import json
    #     return json.dumps(self.serialize_queryset())
