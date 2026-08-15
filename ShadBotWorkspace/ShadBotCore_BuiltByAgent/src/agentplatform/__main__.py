from .domain.immutable_domain import ImmutableDomain
from .application.stateless_application_service import StatelessApplicationService

def main():
    # Initialize the domain layer
    domain_layer = ImmutableDomain({'key': 'value'})

    # Initialize the application service with the domain layer
    app_service = StatelessApplicationService(domain_layer)

    # Process data using the application service
    result = app_service.process_data('input_data')

    print(result)

if __name__ == "__main__":
    main()
