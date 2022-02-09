#include <stdio.h>
#include <stdlib.h>

#include <sys/types.h>
#include <sys/socket.h> // socket functions

#include <netinet/in.h> //structure for storing addresses

int main(){
    char server_message[256] = "Hey, This is text from server."

    //create server socket
    int server_socket;
    server_socket = socket(AF_INET, SOCK_STREAM, 0);

    //specify the server address
    struct sockaddr_in server_address;
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(9002);
    server_address.sin_addr.s_addr = INADDR_ANY;

    //bind the socket to our specified ip and port
    bind(server_socket, (struct sockaddr*) &server_address, sizeof(server_Address));

    listen(server_socket, 5); // number of connections that can be made

    int client_socket;
    client_socket = accept(server_socket,NULL,NULL); // second and third arguement are for information on client tells about its address

    // send the message
    send(client_socket, server_message, sizeof(server_message),0);

    //close the socket
    close(server_socket);
    return 0;
}