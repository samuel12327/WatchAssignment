from Class import Time
import time

def main():
    print("WATCH")
    set_time = Time(00, 00, 00)
    set_time.setTime(00, 00, 00)

    while True:
        set_time.toString()
        action = input("CHOOSE AN ACTION:""\n""SET HOUR""\n""SET MINUTE""\n""SET SECOND""\n""SET TIME""\n""EXIT""\n").upper()
        if action == "SET HOUR":
            hour = int(input("ENTER HOUR: "))
            if hour < 24:
                set_time.setHour(hour)
            else:
                print("ENTER A SMALLER NUMBER")
                time.sleep(1)
        if action == "SET MINUTE":
            minute = int(input("ENTER MINUTE: "))
            if minute < 60:
                set_time.setMinute(minute)
            else:
                print("ENTER A SMALLER NUMBER")
                time.sleep(1)
        if action == "SET SECOND":
            second = input("CHANGE SECOND (+/-): ").upper()
            if set_time.getHour() < 23:
                if set_time.getMinute() < 59:
                    if set_time.getSecond() < 59:
                        if second == "+":
                            set_time.nextSecond()
                        if second == "-":
                            set_time.previousSecond()
                    else:
                        set_time.setSecond(0)
                        set_time.setMinute(set_time.getMinute()+1)
                else:
                    set_time.setSecond(0)
                    set_time.setMinute(0)
                    set_time.setHour(set_time.getHour()+1)
            else:
                set_time.setSecond(0)
                set_time.setMinute(0)
                set_time.setHour(0)
        if action == "SET TIME":
            hour = int(input("ENTER HOUR: "))
            if hour < 24:
                minute = int(input("ENTER MINUTE: "))
                if minute < 60:
                    second = int(input("ENTER SECOND: "))
                    if second < 60:
                        set_time.setTime(hour, minute, second)
            else:
                print("ENTER A SMALLER NUMBER")
                time.sleep(1)
        if action == "EXIT":
            print("EXITING...")
            time.sleep(2)
            break
main()
