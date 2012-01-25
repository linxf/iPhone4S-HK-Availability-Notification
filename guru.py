import re
import wsgiref.handlers
from google.appengine.api import xmpp
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import xmpp_handlers
from google.appengine.api import urlfetch
from google.appengine.api import mail


class XmppHandler(xmpp_handlers.CommandHandler):
  """Handler class for all XMPP activity."""

  def unhandled_command(self, message=None):
    # Show help text
    url = "http://store.apple.com/hk/variationUpdate/IPHONE4S?option.dimensionColor=white&option.dimensionCapacity=16gb&carrierPolicyType=UNLOCKED"
    result = urlfetch.fetch(url)
    if result.status_code == 200:
        doc = result.content
        message.reply(doc)

  def text_message(self, message=None):
    self.unhandled_command(message)

class LatestHandler(webapp.RequestHandler):
  """for test only."""

  def get(self):
    self.response.out.write('ok\n')
    url = "http://store.apple.com/hk/variationUpdate/IPHONE4S?option.dimensionColor=white&option.dimensionCapacity=16gb&carrierPolicyType=UNLOCKED"
    result = urlfetch.fetch(url)
    if result.status_code == 200:
        doc = result.content
	self.response.out.write(doc)
	if (doc.find('isBuyable\":false')<0):
	    if (doc.find('<title>The Apple Store</title>')<0):
                xmpp.send_message('your_gtalk_account@gmail.com', 'iphone 4s 16g white is available. CHECK IT OUT. http://store.apple.com/hk-zh/browse/home/shop_iphone/family/iphone/iphone4s')

def main():
  app = webapp.WSGIApplication([
      ('/', LatestHandler),
      ('/_ah/xmpp/message/chat/', XmppHandler),
      ], debug=True)
  wsgiref.handlers.CGIHandler().run(app)


if __name__ == '__main__':
  main()
