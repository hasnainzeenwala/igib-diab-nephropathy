#!/usr/bin/env python3

##################################################################
## For the given list of proteins print out only the interactions
## between these protein which have medium or higher confidence
## experimental score
##
## Requires requests module:
## type "python -m pip install requests" in command line (win)
## or terminal (mac/linux) to install the module
##################################################################

import requests ## python -m pip install requests
import json

class Protein_Network:
    def __init__(self, gene_list):

        string_api_url = "https://string-db.org/api"
        output_format = "json"
        method = "network"

        ##
        ## Construct URL
        ##

        request_url = "/".join([string_api_url, output_format, method])

        ##
        ## Set parameters
        ##

        my_genes = gene_list

        params = {

            "identifiers" : "%0d".join(my_genes), # your protein
            "species" : 9606, # species NCBI identifier 
            "caller_identity" : "Diabetic Nephropathy Form", # your app name
            "required_score" : 700

        }

        ##
        ## Call STRING
        ##

        response = requests.post(request_url, data=params)

        self.data = json.loads(response.text)


