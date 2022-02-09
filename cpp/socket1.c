#include<stdio.h>
#include<winsock2.h>

#pragma comment(lib,"ws2_32.lib") //Winsock Library

int main()
{
	WSADATA wsa;
	SOCKET s;
    int recv_size;
    // windows way
	if (WSAStartup(MAKEWORD(2,2),&wsa) != 0)
	{
		printf("Failed. Error Code : %d",WSAGetLastError());
		return 1;
	}
	
	// SOCK_STREAM TCP SOCK_DGRAM UDP| 0 (or IPPROTO_TCP, IPPROTO_UDP)
	if((s = socket(AF_INET , SOCK_STREAM , 0 )) == INVALID_SOCKET)
	{
		printf("Could not create socket : %d" , WSAGetLastError());
	}

    //connecting to server
    struct sockaddr_in server;

	server.sin_family = AF_INET; // or AF_INET6
	server.sin_port = htons( 9002 ); // conversion function
	server.sin_addr.s_addr = inet_addr("127.0.0.1");//INADDR_ANY;//inet_addr();

	//Connect to remote server
	int connection_status = connect(s , (struct sockaddr *)&server , sizeof(server));
	if (connection_status < 0){
		puts("connect error");
        printf("%d" , WSAGetLastError());
		return 1;
	}

    //Send some data
	// char message[19] = "GET / HTTP/1.1\r\n\r\n";
	// if( send(s , message , strlen(message) , 0) < 0)
	// {
	// 	puts("Send failed");
	// 	return 1;
	// }
	// puts("Data Send\n");

    //Receive a reply from the server
    char server_reply[2000];
	// while(1){
	// 	int i;
	// 	char server_reply[2000];
	// 	char message[2000];
	// 	cin >> i;
	// 	if(i == 1){
	// 		cin >> message;
	// 		send(s , message , strlen(message) , 0) 
	// 	}
	// }
	if((recv_size = recv(s, server_reply, sizeof(server_reply), 0)) == SOCKET_ERROR){
		puts("recv failed");
	}
	
	puts("Reply received\n");
    server_reply[recv_size] = '\0';
    puts(server_reply);

    closesocket(s);
    WSACleanup();

	return 0;   
}

text(1,2,3), brave, cmd, file, wifi