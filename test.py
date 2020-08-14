from websocket import create_connection
ws = create_connection("ws://irc2ws-bridge.herokuapp.com")
ws = create_connection("ws://localhost:8080")
#ws.send("irc.europnet.org:6667")
ws.send("irc.freenode.net:6667")
print(">> irc.freenode.net:6667")
result =  ws.recv()
print("<< '%s'" % result)

result =  ws.recv()
print("<< '%s'" % result)

ws.send("USER irc2ws_test irc2ws_test irc2ws_test :This is fun bot!\n")
print(">> USER irc2ws_test irc2ws_test irc2ws_test :This is fun bot!\n")

ws.send("NICK irc2ws_test\n")
print(">> NICK irc2ws_test\n")

result =  ws.recv()
print("<< '%s'" % result)

ws.send("JOIN ##test\n")
print(">> JOIN ##test\n")


while(True):
    result =  ws.recv()
    print("<< '%s'" % result)


ws.close()