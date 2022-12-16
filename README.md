# pythonscripts

## 1. Beautiful soup to parse sites + MIME to send mail
#### Ports:
- gmail - 587
- yandex - 465
- mail - 25

If you trying to send mail using `gmail` service, make sure that two-factor authentication is enabled in the account and the application is configured. Instructions on how to do this are on youtube.

How the script works:
1) Parse the html page (for example, hh)
2) Add the found data to the table, and write the table to a file
3) We connect to the mail, form a message and send mail

The `user` and `password` variables are exported at env.
