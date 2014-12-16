from google.appengine.ext import webapp 
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler 
from google.appengine.ext.webapp import util
from google.appengine.api import urlfetch
import json
import logging
import urllib, base64
import models
import settings


def sendNotification(sender, message):
    url = 'https://api.sqwiggle.com/messages'
    data = {
        'stream_id': settings.STREAM_ID,
        'text': message.encode('utf-8'),
        'format': 'html'
    }

    logging.info('data:%s' % data)

    base64string = base64.encodestring('%s:%s' % (settings.AUTH_TOKEN, "X")).replace('\n', '')
    result = urlfetch.fetch(
        url,
        payload=urllib.urlencode(data),
        method=urlfetch.POST,
        headers={"Authorization": "Basic %s" % base64string}
    )

    return json.loads(result.content)

class EmailReceivedHandler(InboundMailHandler):

    ''' receives inbound email, logs it, stores the contents, then forwards to Sqwiggle using the API. '''
    def receive(self, mail_message):
        logging.info ('Received email from %s' % mail_message.sender) 
        ''' TODO: add in exception handling '''
        email = models.EmailNotification()
        email.email_sender = mail_message.sender
        email.email_subject = mail_message.subject
        ''' HACK ALERT '''
        bodies = mail_message.bodies(0)
        for content_type, body in bodies:
           email.email_body = body.decode()
        email.put()
        ''' sends the notification, including a link to the email.'''
        notification = '%s [<a href="http://%s/message/%s">view</a>]' % \
                       (email.email_subject, settings.DOMAIN, email.key().id_or_name())
        logging.info ('Sending Sqwiggle notification: %s' % sendNotification ( mail_message.sender, notification ))
        
def main():
    application = webapp.WSGIApplication([EmailReceivedHandler.mapping()], debug=settings.DEBUG)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()


