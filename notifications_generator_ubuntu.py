import gi
gi.require_version('Notify', '0.7')

from gi.repository import Notify
Notify.init("App Name")
notify=Notify.Notification.new("Notifications",     #message
"visit \n<u>https://www.devdungeon.com/content/desktop-notifications-linux-python</u>")

#notify.set_urgency(2)      #urgency
notify.set_urgency(0)

notify.show()       #show notification
#yo eauta comment ho 
