## Sentry - Papertrail Alerts via SMS

### Introduction

Sentry accepts Papertrail events (posted via the Webhook alerts) and sends them as SMS messages to your phone via Twilio.

There are numerous uses for this:

- get an SMS whenever someone uses root to log into SSH
- get an SMS whenever your web application crashes
- get an SMS whenever Nginx or another service goes down
- etc.

You can pretty much adapt this to any situation.

### Why?

I recently got hooked on Papertrail. I love their search alerts - you can get an alert whenever a certain string of text shows up in the logs. They had several options for sending you alerts: 

- email
- webhook
- campfire
- etc.

But, no SMS. Sentry fixes that.

### Configuration

#### Sentry Side:

Install `flask` and `twilio`:

    pip install -r requirements.txt

Change the Twilio Settings in `app.py`:

    account_sid  = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    auth_token   = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    phone_number = "+1XXXXXXXXXX"
    from_number  = "+1XXXXXXXXXX" 

Run it:

    python app.py

If you want to run it on Heroku (as I did), just add the `Procfile` and push it to Heroku.

#### Papertrail Side:

The first step is to setup an alert - [there's a tutorial here](http://help.papertrailapp.com/kb/how-it-works/alerts).

Then, set the Webhook for the alert to [domain.com/sentry](), the URL for the Sentry app. I would suggest settings the Frequency to Every Minute so that you get alerts as fast as possible.

### License
Zinc is open source and is distributed under the MIT License:

	Copyright © 2012 Mihir Singh <me@mihirsingh.com>

	Permission is hereby granted, free of charge, to any person obtaining a copy of 
	this software and associated documentation files (the "Software"), to deal in 
	the Software without restriction, including without limitation the rights to 
	use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of 
	the Software, and to permit persons to whom the Software is furnished to do 
	so, subject to the following conditions:

	The above copyright notice and this permission notice shall be included in all 
	copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED â€œAS ISâ€, WITHOUT WARRANTY OF ANY 
	KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
	WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
	PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
	DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
	CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
	CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
	IN THE SOFTWARE.
	
### Contributing
Just fork and submit a pull request ;)
