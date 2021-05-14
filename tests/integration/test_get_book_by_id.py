import http.client


class TestGetBookById:

    def test_should_return_http_status_200_and_book(self):
        connection = http.client.HTTPConnection('localhost:3000')
        connection.request(method="GET", url="/dev/books/5fbd8453-dd36-4e58-8a1b-3229e70bcef3")

        response = connection.getresponse()

        assert response.status == 200
