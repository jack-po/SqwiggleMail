# SqwiggleMail notifiier

SqwiggleMail is an [Google App Engine][] application for sending notifications to [Sqwiggle][].

It does the following:

1. Defines an email endpoint for receiving emails.
2. Sends a notification of a new email to the appropriate [Sqwiggle][] room, using the email subject as the message.
3. Stores the body of the email in the AppEngine datastore.
4. Provides a link in the [Sqwiggle][] notification to the original email.

Setup settings for your application to **app.yaml** and **setting.py** files and then deploy to **GAE**. See **streams.py** file for finding your stream id at **Sqwiggle**.

The email address to which to send the notifications will depend on the AppEngine app_id you use in **app.yaml** - more details can be found on the Google help site [here](http://code.google.com/appengine/docs/python/mail/receivingmail.html).

[Sqwiggle]: https://www.sqwiggle.com/
[Google App Engine]: https://cloud.google.com/appengine/