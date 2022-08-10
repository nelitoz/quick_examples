"""
To make it work, first:
1. Create an account in imbd-api.com to get an API key
2. Create an accouunt  in swagger for swagger hub (Enterprise Trial)
 2.1 Make sure you have a Domain in Swagger hub
 2.2 Import and document API from swagger hub based on the next URL: https://imdb-api.com/swagger/IMDb-API/swagger.json
 2.3 Export Client SDK as python code
3. Unzip the SDK archive
4. Modify line 49 from file swagger_client/configuration.py to add host "https://imdb-api.com/en"
5. Install module requirementes define in the SDK folder downloaded (pip install requirements.txt)
5. Proceed to install the SDK (python setup.py install )
6. Start testing

There is an SDK repo in https://github.com/nelitoz/IMDB/tree/main/swagger_client
"""
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import click

# create an instance of the API class
api_instance = swagger_client.MoviesApiApi()
api_key = '---' # str| add the proper key you got from your imdb-api account

@click.group()
def cli():
    """ Get valuable information from imdb """
    pass

@click.command()
def get_250():
    """ return the 250 best movies all time"""
    try:
        api_response = api_instance.a_pi_top250_t_vs_api_key_get(api_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MoviesApiApi->a_pi_top250_t_vs_api_key_get: %s\n" % e)

@click.command()
def box_office():
    """ return the box office """ 
    try:
        api_response = api_instance.a_pi_box_office_api_key_get(api_key)
        pprint(api_response)
    except:
        print("Exception in box office")

@click.command()
def in_theaters():
    """ return the movies still on theaters""" 
    try:
        api_response = api_instance.a_pi_in_theaters_api_key_get(api_key)
        pprint(api_response)
    except:
        print("Exception in theaters")


cli.add_command(get_250)
cli.add_command(box_office)
cli.add_command(in_theaters)


if __name__ == "__main__":
    cli()
