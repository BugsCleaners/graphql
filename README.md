# graphql
GraphQL basic sample
This is a simple basic graphql server and consumer written in python(flask), where the server-side is containerized and deploiyed as a container.
Tutorial:  
1- Dwonload the files from github  
2- run the following command in the "graphql" folder to build the image:  
  docker build -t my-graphql-app . 
3- Run the following command to run the container and expose port 5000 on the localhost:  
  docker run -p 5000:5000 my-graphql-app  
4- Run the following command in the "graphql client" folder to consume the service:  
   python .\test.py  
5- You should have your response😊  
P.S: You could run the server on your local machine without containerization by using the "app.py" file and the following command:  
  python app.py  
Sample response:  
  ![response](https://github.com/BugsCleaners/graphql/assets/91881471/0ffbcce0-25f5-4194-a551-0879c8978c37)
