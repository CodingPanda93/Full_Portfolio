1. Load package.json with all modules needed for project (body-parser, express, socket.io, ejs)
2. Make views/routes/static directories
3. Install npm
4. Make server.js with module exports and route structure

5. Have server when get("/"), load index.ejs, and prompt user for name
6. Have client EMIT "new_user" to server to add user to site
7. Have server listen for "new_user" to add user to "users" variable (req.data.name)
8. Have server EMIT "conversation_board" with all past messages within variable "conversation_messages"
9. Have client listen for "conversation_board" to load conversation board HTML with "conversation_messages" data
10. Have client EMIT "new_message" with message content to server whenever "Send" is clicked
11. Have server listen for "new_message" and add message with "name/session_id" into "conversation_messages" data
12. Have server FULL_BROADCAST "update_conversation_messages" with "conversation_messages" data
13. Have client listen for "update_conversation_messages" with "conversation_messages" data 
