# SpeedTestPythonServerClient
Server and Client for a local speed test

Run this server with my Android SpeedTest app
https://github.com/fbelik/SpeedTest

Server run as with following:
./speedServer.py [IP-ADDR] [PORT-NUM]
Server will then listen and can accept multiple requests at once

Python client runs with following:
./speedClient.py [IP-ADDR] [PORT-NUM] [NUM-CHUNKS]
Client will request certain number of chunks from server which will 
be sent and timed for a network speed

Kotlin client with following:
kotlinc speedClient.kt
kotlin SpeedClientKt [IP-ADDR] [PORT-NUM] [NUM-CHUNKS]
Operates the same way as python client. Implemented in android application
listed above at https://github.com/fbelik/SpeedTest
