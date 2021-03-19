from py2neo import Graph

# create venv
    # on windows: py -m virtualenv venv (or equivalent)
# start venv
    # on windows: .\\\\venv\\scripts\\activate.ps1
# install python packages via requirements file 
# OR just pip install py2neo
    # on windows: py -m pip install -r requirements.txt (or equivalent)
# start up your local database in Neo4j
# run file & enter credentials to database

def test(graph, label):
    # get full nodes with a specific label
    query = """MATCH (n:{}) RETURN DISTINCT n LIMIT 10""".format(label)
    nodes = graph.run(query).data()
    print("##### NODES #####")
    print(nodes)
    # get all properties for nodes with a specific label
    properties = [x['properties'] for x in graph.run("""MATCH (n:{}) UNWIND keys(n) AS properties RETURN DISTINCT properties""".format(label)).data()]
    print("##### PROPERTIES #####")
    print(properties)
    # get the first property in "properties" list for nodes with a specific label
    nodes = [x['node'] for x in graph.run("""MATCH (n:{}) RETURN DISTINCT n.{} AS node LIMIT 10""".format(label, properties[0])).data()]
    print("##### PROPERTY OF NODES #####")
    print(nodes)


if __name__ == "__main__":
    port = input("Enter Neo4j DB Port: ")
    user = input("Enter Neo4j DB Username: ")
    pswd = input("Enter Neo4j DB Password: ")
    try:
        graph = Graph('bolt://localhost:'+port, auth=(user, pswd))
        print("Connected to the local graph database.")
        label = input("Enter a label in your database, verbatim: ")
        test(graph, label)
    except:
        print("Could not connect to the local graph database.")
        quit()
