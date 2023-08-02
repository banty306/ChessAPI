# ChessAPI
A simple chess app with some basic APIs. 



## Getting Started

1. Clone the ChessAPI repository from GitHub using the following command: 
```shell
git clone https://github.com/banty306/ChessAPI.git
```
2. Change the working directory to the ChessAPI folder:
```shell
 cd ChessAPI
```
3. Run the Docker containers using docker-compose:
```shell
docker-compose up -d or sudo docker-compose up
```
***
Please do verify by now the containers should be up and running. 


***
# CURLS

```http request
curl --location 'localhost:8000/api/v1/chess/queen' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=0zkaYrpXdhPw5Hdlg6OXwGUJv1TCOhOF3wGsu2wTasooKsQkIEhQIh2j7DbR9EGz' \
--data '{"positions": {"Queen": "H1", "Bishop": "B7", "Rook":"H8", "Knight": "F2"}}'
```
```text
Response
{
    "valid moves": [
        "B7",
        "G1",
        "F1",
        "E1",
        "C1",
        "B1",
        "A1",
        "H8"
    ]
}
```

```http request
curl --location 'localhost:8000/api/v1/chess/knight' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=0zkaYrpXdhPw5Hdlg6OXwGUJv1TCOhOF3wGsu2wTasooKsQkIEhQIh2j7DbR9EGz' \
--data '{"positions": {"Queen": "E7", "Bishop": "B7", "Rook":"G5", "Knight": "C3"}}'
```
```text
Response
{
    "valid moves": [
        "A2",
        "A4",
        "B1",
        "D1"
    ]
}
```

```http request
curl --location 'localhost:8000/api/v1/chess/rook' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=0zkaYrpXdhPw5Hdlg6OXwGUJv1TCOhOF3wGsu2wTasooKsQkIEhQIh2j7DbR9EGz' \
--data '{"positions": {"Queen": "A5", "Bishop": "G8", "Rook":"H5", "Knight": "G4"}}'
```
```text
Response
{
    "valid moves": [
        "A5",
        "H4",
        "H3",
        "H1",
        "H8"
    ]
}
```

```http request
curl --location 'localhost:8000/api/v1/chess/bishop' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=0zkaYrpXdhPw5Hdlg6OXwGUJv1TCOhOF3wGsu2wTasooKsQkIEhQIh2j7DbR9EGz' \
--data '{"positions": {"Queen": "H3", "Bishop": "B2", "Rook":"H8", "Knight": "F2"}}'
```
```text
Response
{
    "valid moves": [
        "A1",
        "C1",
        "D4",
        "E5",
        "F6",
        "G7"
    ]
}
```


