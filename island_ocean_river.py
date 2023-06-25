#1
import os
import json

#2
from abc import ABC

#3
class BrandingAgency(ABC):
    """
    Abstract base class for a branding agency.
    """

    #4
    def __init__(self):
        self.client_data = {}

    #5
    def add_client(self, client_name, client_data):
        """
        Adds a new client to the client data dict.

        The client data should include a "strategy" and
        a "style" key.
        """
        self.client_data[client_name] = client_data

    #6
    def save_client_data(self):
        """
        Saves the client data dict to a json file.
        """
        with open('client_data.json', 'w') as f:
            json.dump(self.client_data, f, indent=4)

    #7
    def load_client_data(self):
        """
        Loads the client data json file.
        """
        with open('client_data.json', 'r') as f:
            self.client_data = json.load(f)

    #8
    def create_strategy(self, client_name):
        """
        Abstract method for subclass to implement to create a
        strategy for a given client.
        """
        raise NotImplementedError("Please Implement this method")

    #9
    def create_style(self, client_name):
        """
        Abstract method for subclass to implement to create a
        style for a given client.
        """
        raise NotImplementedError("Please Implement this method")

    #10
    def help_business_stand_out(self, client_name):
        """
        Creates a strategy and a style for a given client
        and saves the data to the client_data dict and
        the json file.
        """
        strategy = self.create_strategy(client_name)
        style = self.create_style(client_name)
        self.add_client(client_name,
                        {'strategy': strategy,
                         'style': style})
        self.save_client_data()


#11
class InnovativeStrategyAgency(BrandingAgency):
    """
    A subclass of BrandingAgency that specializes in
    creating innovative strategies.
    """

    #12
    def create_strategy(self, client_name):
        """
        Creates an innovative strategy for a given client.
        Returns a string with the strategy.
        """
        return f'Innovative strategy for {client_name}.'

    #13
    def create_style(self, client_name):
        """
        Creates a style for a given client.
        Returns a string with the style.
        """
        return f'Style for {client_name}.'

#14
if __name__ == '__main__':
    #15
    agency = InnovativeStrategyAgency()

    #16
    agency.help_business_stand_out('Business A')
    agency.help_business_stand_out('Business B')

    #17
    agency.load_client_data()  # Loads the json file.

#18
    print(agency.client_data)  # Prints the dictionary.