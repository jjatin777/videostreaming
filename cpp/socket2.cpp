#include<io.h>
#include<stdio.h>
#include<winsock2.h>
#include<string>

#pragma comment(lib,"ws2_32.lib") //Winsock Library
using namespace std;
int main()
{
	WSADATA wsa;
	SOCKET s;
	// struct sockaddr_in client;
	int c;
	char* message;

	if (WSAStartup(MAKEWORD(2,2),&wsa) != 0){
		printf("Failed. Error Code : %d",WSAGetLastError());
		return 1;
	}
	
	//Create a socket
	if((s = socket(AF_INET , SOCK_STREAM , 0 )) == INVALID_SOCKET){
		printf("Could not create socket : %d" , WSAGetLastError());
	}

	int PASCAL WSAAsyncSelect(s,HWND,u_int,long);

	//Prepare the sockaddr_in structure
	struct sockaddr_in server;

	server.sin_family = AF_INET;
	server.sin_port = htons( 9002 );
	server.sin_addr.s_addr = inet_addr("127.0.0.1");//htonl(INADDR_ANY)//inet_addr("127.0.0.1");

    // char *server_ip = inet_ntoa(server.sin_addr);
    // printf("%s\n",server_ip);
	
	//Bind
	if( bind(s, (struct sockaddr *)&server , sizeof(server)) == SOCKET_ERROR){
		printf("Bind failed with error code : %d" , WSAGetLastError());
	}

	//Listen to incoming connections
	listen(s, 5);
	
	//Accept and incoming connection
	puts("Waiting for incoming connections...");
	
	// c = sizeof(struct sockaddr_in);
	// new_socket = accept(s , (struct sockaddr *)&client, &c);

	SOCKET client_socket;
    client_socket = accept(s, NULL, NULL);
	if (client_socket == INVALID_SOCKET){
		printf("accept failed with error code : %d" , WSAGetLastError());
	}
	
	puts("Connection accepted");
    // char *client_ip = inet_ntoa(client.sin_addr);
    // int client_port = ntohs(client.sin_port);

	//Reply to client
	message = "Hello Client , I have received your connection. But I have to go now, bye\n";
	send(client_socket, message, strlen(message) , 0);
	
	// getchar();
	puts("done");
	closesocket(s);
	WSACleanup();
	
	return 0;
}

// g++ socket1.c -o client.exe -lwsock32