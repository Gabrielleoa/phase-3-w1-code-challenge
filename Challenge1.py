def converting_time(hour, minutes, time_period):
    if not(1<= hour <= 12) or not (0<= minutes <=59) or time_period not in ['am', 'pm']:
        return 'Not time'
    if time_period == 'pm' and hour != 12:
        hour+= 12
    elif time_period == 'am' and hour == 12:
        hour = 00

    resulting_hour= (f"{hour:00}")
    resulting_minute=(f"{minutes:00}")

    return resulting_hour+resulting_minute

print(converting_time(5,45, 'pm'))
print(converting_time(8,25,'am'))