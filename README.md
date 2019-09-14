# color-repo

A small python service for storing and retrieving color information.



## Objective

The primary objective of this application is to provide a back-end service for [color-notebook](https://github.com/WalterHahn/color-notebook).



## Usage


```
$ pip install flask,flask-cors,mysql
$ export FLASK_APP=index.py
$ python -m flask run
```

1. **color-repo** utilizes a mysql database.  Run `install.sql` to initialize schema.
2. **color-repo** depends on *flask* and *mysql*.
3. In a windows environment, instead use `set FLASK_APP=index.py`, to set the environment variable.
4. The service runs on port `5000` by default.



## API

| Method | Endpoint | Parameters                    | Description                               |
| ------ | -------- | ----------------------------- | ----------------------------------------- |
| GET    | /        | n/a                           | Returns all colors.                       |
| PUT    | /        | { name: string, hex: string } | Creates a new color in the repository.    |
| DELETE | /        | { color_id: int }             | Deletes a color from the repository.      |
| POST   | /search  | { query: string }             | Returns colors with names matching query. |



  ## Database

### color_repo

#### colors

| Column     | Type                               | Description                          |
| ---------- | ---------------------------------- | ------------------------------------ |
| color_id   | int(11) PRIMARY KEY AUTO_INCREMENT | Primary identifier                   |
| created_at | DATETIME                           | Date row was inserted                |
| name       | varchar(32)                        | Name of color                        |
| hex        | varchar(6)                         | Six character hexadecimal color code |

