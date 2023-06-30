import ast
import base64

### Azure DevOps organization and project details ###

organization = "YOUR ORGANIZATION"  # Sua organização#
project = "YOUR PROJECT"  # seu projeto#
team = "YOUR TEAM"  # seu time#

### Personal access token (PAT) with appropriate permissions ###
pat = "PERSONAL ACESS TOKEN"  # seu personal acess token#
b64_pat = base64.b64encode(bytes(":" + pat, "ascii")).decode("ascii")
headers = {"Accept": "application/json", "Authorization": "Basic " + b64_pat}
