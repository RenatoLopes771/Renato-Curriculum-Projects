def add_time(start, duration, startingday=False):

    def convert(to_convert, logic=False):
        # converts to 24 hour format

        extra = 0
        if logic:

            to_convert = to_convert.split()

            if to_convert[1] == "PM":
                extra = 1200
            
            to_convert = to_convert[0].split(":")
            
        else:
            to_convert = to_convert.split(":")
        
        to_convert = to_convert[0] + to_convert[1]

        return int(to_convert) + extra
    

    def time_calculator(start, duration):
        

        global days
        days = 0

        start = start + duration

        while start >= 2400:
            start = start - 2400
            days = days + 1

        if int(str(start)[-2:]) >= 60:
            start = start + 40

        if start >= 2400:
            start = start - 2400
            days = days + 1

        return start


    def day_table(day, passed):
        # Returns the day based on how many days passed since then

        day = day.lower()

        if passed:
            if day == "monday":
                return day_table("Tuesday", passed - 1)
            elif day == "tuesday":
                return day_table("Wednesday", passed - 1)
            elif day == "wednesday":
                return day_table("Thursday", passed - 1)
            elif day == "thursday":
                return day_table("Friday", passed - 1)
            elif day == "friday":
                return day_table("Saturday", passed - 1)
            elif day == "saturday":
                return day_table("Sunday", passed - 1)
            elif day == "sunday":
                return day_table("Monday", passed - 1)
        else:
            return day.capitalize()


    def convert_back(the_time):
        #converts to 12 hour format
        global ampm

        if the_time >= 1200:
            if the_time >= 1300:
                the_time = the_time - 1200
            ampm = "PM"
        else:
            if the_time < 100:
                the_time = the_time + 1200
            ampm = "AM"

        if the_time:
            the_time = str(the_time)

            if len(the_time) == 4:
                time1 = the_time[0:2]
                time2 = the_time[2:]
                return f"{time1}:{time2}"

            elif len(the_time) == 3:
                time1 = the_time[0]
                time2 = the_time[1:]
                return f"{time1}:{time2}"

            elif len(the_time) == 2:
                return f"00:{the_time}"

            elif len(the_time) == 1:
                return f"00:0{the_time}"

        
        else: # 0
            return "00:00"


    total = time_calculator(convert(start, True), convert(duration))
    #print(time_calculator(convert(start, True), convert(duration)))
    

    final_time = convert_back(total)

    if startingday: # Specifies day

        final_day = day_table(startingday, days)

        if days == 1: # A day passed
            # add_time("10:10 PM", "3:30")
            # Returns: 1:40 AM (next day)
            extra = f", {final_day} (next day)"
        elif days > 1: # More than a day has passed
            # add_time("11:43 PM", "24:20", "tueSday")
            # Returns: 12:03 AM, Thursday (2 days later)
            extra = f", {final_day} ({days} days later)"
        else: # No days passed
            # add_time("11:30 AM", "2:32", "Monday")
            # Returns: 2:02 PM, Monday
            extra = f", {final_day}"

    else: # Doesn't specify day
        if days == 1: # '''
            extra = " (next day)"
            
        elif days > 1: # '''
            # add_time("6:30 PM", "205:12")
            # Returns: 7:42 AM (9 days later)
            extra = f" ({days} days later)"

        else: # '''
            #add_time("3:00 PM", "3:10")
            # Returns: 6:10 PM
            extra = ""

    return f"{final_time} {ampm}{extra}"