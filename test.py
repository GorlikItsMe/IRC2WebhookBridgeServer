from websocket import create_connection
ws = create_connection("ws://localhost:1988/")
#ws.send("irc.europnet.org:6667")
ws.send("irc.freenode.net:6667")
print(">> irc.freenode.net:6667")
result =  ws.recv()
print("<< '%s'" % result)

result =  ws.recv()
print("<< '%s'" % result)

ws.send("USER gkill_test gkill_test gkill_test :This is fun bot!\n")
print(">> USER gkill_test gkill_test gkill_test :This is fun bot!\n")

ws.send("NICK gkill_test\n")
print(">> NICK gkill_test\n")

result =  ws.recv()
print("<< '%s'" % result)

ws.send("JOIN ##test\n")
print(">> JOIN ##test\n")


while(True):
    result =  ws.recv()
    print("<< '%s'" % result)


ws.close()