import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title = "**Drink Water**",
        message = "If you don’t get enough water, you can become dehydrated. "
                  "Severe cases of dehydration can cause dizziness, confusion, and even seizures.",
        app_icon ="water.ico",
        timeout = 10

    )
