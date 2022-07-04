import pystray

from PIL import Image

class quickBTConnect():
    def exitAction(self):
        self.qbt.stop()

    def action(self):
        #TODO all main code
        print("Action!")

    def __init__(self, icon_path):
        #TODO Icona presa da icon8, verificare come comportarsi con diritti
        qbt_sys_tray_icon = Image.open(icon_path)
        qbt_menu = pystray.Menu(
                    pystray.MenuItem("Action", self.action),
                    pystray.MenuItem("Exit", self.exitAction))
        self.qbt = pystray.Icon(
                            name = "qbt_icon", 
                            icon = qbt_sys_tray_icon,
                            title = "Quick BT Connect", 
                            menu = qbt_menu,
                            visible = True)
        self.qbt.run()

app = quickBTConnect("icon.png")