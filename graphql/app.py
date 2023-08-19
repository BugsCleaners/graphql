from flask import Flask, jsonify, request
import graphene

app = Flask(__name__)

class Query(graphene.ObjectType):
    hello = graphene.String(description="A simple greeting")

    def resolve_hello(self, info):
        return "Hello, GraphQL!"
#class Query(graphene.ObjectType):
    test = graphene.String(description="A simple test")

    def resolve_test(self, info):
        return "test, completed"

schema = graphene.Schema(query=Query)

@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    result = schema.execute(data.get('query'))
    return jsonify(result.data)

if __name__ == '__main__':
    app.run(host="0.0.0.0",)
