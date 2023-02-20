# Simple async price alarm app with Python and MongoDB

Works behind a reverse proxy, it supports subdirectories
In real use, this app is behind basic authentication (managed by Nginx)

Checks every 30 minutes if there are changes in the given URLs. If there are price changes and they fall in the given range, an email notification is sent.