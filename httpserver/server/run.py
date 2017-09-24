import socket
import os

def get_response(request):
    request = request.decode()
    try:
        begin = request.index(' ')
    except ValueError:
        return "HTTP/1.1 200 OK\r\n\r\n".encode()
    if (request[:begin] != "GET"):
        return "HTTP/1.1 405 Method Not Allowed\r\n\r\n".encode()
    try:
        end = request.index(' ', begin + 1)
    except ValueError:
        return "HTTP/1.1 200 OK\r\n\r\n".encode()

    begin += 1
    action = request[begin:end]
    if (action == '/'):
        usr_pos = request.index('User-Agent')
        usr = request[usr_pos + 12:].split()[0]
        return ("HTTP/1.1 200 OK\r\n\r\n" + 'Hello mister!\nYou are {}'.format(usr)).encode()
    elif (action.startswith('/media')):
        if (action == '/media'):
            result = "HTTP/1.1 200 OK\r\n\r\n".encode()
            for f in os.listdir("files"):
                path = "files/" + f
                if (os.path.exists(path)):
                    with open(path, 'rb') as file:
                        result += f.encode() +  "\n\n".encode() + file.read() + "\n".encode()
            return  result
        else:
            filename = action[action.index('/', 1):]
            path = "files" + filename
            if (os.path.exists(path)):
                with open(path, 'rb') as file:
                    result = "HTTP/1.1 200 OK\r\n\r\n".encode() + file.read()
                    return result
            else:
                return "HTTP/1.1 404 Not found\r\n\r\n".encode() + "No such file\n".encode()
    elif (action == "/test"):
        return "HTTP/1.1 200 OK\r\n\r\n".encode() + request.encode()
    else:
        return "HTTP/1.1 404 Not found\r\n\r\n".encode() + "Using unknown option\n".encode()
    return "HTTP/1.1 404 Not found\r\n\r\n".encode()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  #Привязываем к сокету имя хоста и номер порта.
server_socket.listen(0)  #Ждем подключений клиентов к сокету, параметр - число клиентов,
#которые могут стоять в очереди на подключение.

print ('Started')

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print ('Got new client', client_socket.getsockname())  #Выводим IP хозяина клиентского сокета,
        # подключившегося к серверу.
        request_string = client_socket.recv(2048)  #Получаем данные (в данном случае,
        #Get-запрос) от клиентского сокета (максимум 2048 байт - размер буфера).
        response = get_response(request_string)
        client_socket.send(response)  #Отправляем ответ.
    except KeyboardInterrupt:  #Останавливаем сервер вручную (например, остановить выполнение программы в Idea).
        print ('Stopped')
        server_socket.close()  #Закрываем сокет.
        exit()

