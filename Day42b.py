import winsound
import datetime


def ser_alarm():
    hour = input('Please enter hour: ')
    minute = input('Please enter minute: ')
    alarm_time = hour + ':' + minute
    print('You have set alarm for', alarm_time)

    while True:59
        now = datetime.datetime.now().strftime("%H:%M")
        if alarm_time == now:
            print('Wake up')
            print('Wake up')
            print('Wake up')
            winsound.PlaySound('SystemExit', winsound.SND_ALIAS)
            break


ser_alarm()

