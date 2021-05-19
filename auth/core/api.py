from flask_restx import Resource as RestResource


class Resource(RestResource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.services = self.api.services
