# MarkLundager.com

marklundager.com is a website which I work on when I find the time. Currently, the frontend is implemented using React and the backend is implemented with Python. It is hosted on my Raspberry Pi 4 which is
connected to an arduino which in turn is connected to 4 controllable LEDs. I use NGINX as a reversed proxy to handle encryption (SSL), redirects and potential work load balances in the future. Listed below are features which I have added (marked Done)
and features I wish to implement. Additionally, the website is not tailored to handle accesses from a smartphone.

# Ideas/Todo:

- Add NGINX as reverse proxy to encrypt with SSL (DONE)
- Create SQL Database system for users & Lamp - authority association(DONE)
- Restrict access based on account system (DONE)
- Create SQL table mapping authority to accesses (DONE)
- Add Password matching error on creating account when passwords do not match (DONE)
- Create Project section
- Create About Me section
- check status code of every response and make sure it is in align with the conventions (PROGRESS)
- Handle communication between client and server better in order to inform users better  (PROGRESS)
- Structure backend better, especially regarding login_manager  (PROGRESS)
- Add requirements on password and username (length, characters etc.)  (PROGRESS)
- Create admin page to handle authorities.  (PROGRESS)
- Fix resolution on stream  (PROGRESS)
- Create chat system
- Make webpage mobile friendly
