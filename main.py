from http.server import BaseHTTPRequestHandler, HTTPServer

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """Специальный класс, который отвечает за обработку входящих запросов от клиентов"""

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Отправка типа данных
        self.end_headers()  # Завершение формирования заголовков ответа

        # Чтение содержимого файла contact.html и отправка его в ответе
        try:
            with open("contact.html", "r", encoding="utf-8") as file:
                content = file.read()
                self.wfile.write(bytes(content, "utf-8"))  # Тело ответа
        except FileNotFoundError:
            self.wfile.write(bytes("<h1>404 Not Found</h1>", "utf-8"))

    def do_POST(self):
        """ Метод для обработки входящих POST-запросов """
        content_length = int(self.headers['Content-Length'])  # Получаем длину данных
        post_data = self.rfile.read(content_length)  # Читаем данные из запроса

        print("Received POST data:", post_data.decode('utf-8'))  # Печатаем данные в консоль

        self.send_response(200)  # Отправляем ответ клиенту
        self.end_headers()
        self.wfile.write(bytes("Data received", "utf-8"))  # Ответ клиенту


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")