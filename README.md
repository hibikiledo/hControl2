# hControl2
hControl2 : control your home from the distant.

###About This Project

Home automation has always been my dream. With today's technologies, it can be done relatively easy.  
This project allow me to control my home from a distant.  

Now, I'm using this project to control spotlight from my smartphone.  
You may wonder why I need to use it for such purpose. The answer is simple. It's **FUN**!


###Architecture

#####Server
The server runs web server written in python with Flask framework.  
House states is kept inside **hstates** module where values can be changed from the API.  
Server provides API for both arduino and web interface to access/modify house states.

#####Files related to server side
- hcontrol2.py : main script
- hauth.py : provide basic authentication
- hstates.py : add, remove, get, set the states of objects in house
- hutils.py : collection of utility functions

#####Client
Client is the web interface written with HTML, CSS, jQuery2, and Bootstrap.
Client connects to the server via the API to set / get information from the server.

#####Arduino
Connect to the server via Ethernet shield.  
It use API to only **read** house state from the server.

#####Files related to client side
- template/index.html : web interface
- static/style.css : stylesheet

### Configurations

#### Authentication
Open file hauth.py and change PUB_KEY and AUTH_TOKEN  
PUB_KEY is the passphrase required when accessing the web interface.  
AUTH_TOKEN is the token returned from server if the PUB_KEY is correct.

### Turn off debug mode
Open file hcontrol2.py, scroll down and change  
app.run(debug=True) to app.run(host='0.0.0.0')

### Add more objects
Now, hstates.py implement 2 class of objects which are OUTDOOR and INDOOR.
You may add more object by using function
- hstates.add(object, group) : add new object to the group

You may look at hcontrol2.py as an example.

##Remarks
I would save this is an incomplete work.  
I haven't tested it thoroughly, so there are bugs hidden somewhere for sure.

## Happy Coding ._.
