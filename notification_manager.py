import smtplib

my_email = "zmssmzx@gmail.com"
password = "lyqi vxqn qfhq usty"
the_other_email = "xyz101abc321@yahoo.com"
email_juan = "juanfcr11@gmail.com"


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""
    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email_juan,
                msg=message
            )
