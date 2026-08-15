class StatelessApplicationService:
    def __init__(self, domain_layer):
        self.domain_layer = domain_layer

    def process_data(self, data):
        return self.domain_layer.data(data)
