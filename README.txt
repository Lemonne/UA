The take-home exercise for UA.
Author: Nerissa Lemon

The problem space:
As a Platform Engineer at Urban Airship, you'll be building and maintaining
  distributed systems that support billions of requests per day.
  We provide RESTful APIs for our backend tiers as well as backend RPC services
  that must be highly available and scalable. The systems that you will be
  designing/maintaining will follow the concept of service-oriented architecture.

I chose to minimally implement the Finger RFC because it had an easier to follow
  RFC, and there was examples on the internet for me to gain a better context
  for the problem. I don't have a lot of experience with networking or databases,
  and as such the majority of my time was spent researching and learning for
  this problem.
The main code takes in a request, liberally parses it, and either forwards a
  request on, or serviced locally. At either the host, which is a logged in
  user, just this [local] user. Then, it displays whatever data was received
  to the user.
I chose to implement the features of parsing, as that was at the core of the
  problem. I also wanted to be able to forward a request because that was
  something in the RFC that was a "must".
If I were to do this project again, I would make the code more efficient, as
  the code does not deal with network time-outs or error handling. The parser
  currently decomposes the hosts into a list, and then rebuilds a string for
  forwarding.  While good for validation, if I was focused on efficiency rather
  than safety, an alternate option would simply forward the string after
  stripping off the last host.
  

note: this is also on github, available to see at https://github.com/Lemonne/UA
