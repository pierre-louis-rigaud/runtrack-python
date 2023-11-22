def time_to_text(minutes):
    heures = minutes // 60
    minutes = minutes % 60
    print(f'{heures} heure(s) et {minutes} minutes')


time_to_text(65)
time_to_text(135)
time_to_text(195)
time_to_text(256961)
time_to_text(180000)
