# pythonscripts

## 1. Beautiful soup to parse sites + MIME to send mail
#### Ports:
- gmail - 587
- yandex - 465
- mail - 25

If you trying to send mail using `gmail` service, make sure that two-factor authentication is enabled in the account and the application is configured. Instructions on how to do this are on youtube.

#### How the script works:
1) Parse the html page (for example, hh)
2) Add the found data to the table, and write the table to a file
3) We connect to the mail, form a message and send mail

The `user` and `password` variables are exported at env.


## 2. Matplotlib to make graph and shell script to get the values we need
#### How does it work:
1) `crontab` or service (service is better) runs the `.sh` script after we login and writes the values to the file
2) We read the numbers line by line and create a graph using the module mathplotlib
