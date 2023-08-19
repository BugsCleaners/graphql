import requests

# Define the GraphQL query
query = """
{
    hello
    test
}
"""

# Set the endpoint URL
url = 'http://localhost:5000/graphql'

# Send the query to the GraphQL server
response = requests.post(url, json={'query': query})
data = response.json()

# Print the response
print(data)
