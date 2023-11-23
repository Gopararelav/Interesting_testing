import socket


def send_f(request: str):
    request = request.split(sep=" ")
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    # PIC = 'HTTP/1.1 200 \r\nContent-Type: image/*\n\n'
    if request[0] == "GET" and request[1] == "/":
        conn.send(HDRS.encode() + """<title>HI</title>""".encode())
        conn.send("""<img src="Button.png">""".encode())
        conn.send("""<audio controls src="Bpple.mp3">""".encode())
    elif request[0] == "GET":
        with open(request[1][1:], "br") as file:
            conn.send(HDRS.encode() + file.read())
    elif request[0] == "POST":
        with open(request[1][1:], "br") as file:
            print(request[-1][11:])
            conn.send(HDRS.encode() + file.read())
    conn.close()
    return


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server started...")
s.bind(("192.168.1.43", 80))
s.listen(4)
while True:
    conn, dr = s.accept()
    with conn:
        data = conn.recv(1024)
        if not data:
            conn.close()
        send_f(data.decode())
