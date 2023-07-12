best_scores = [{'first_name': 'Kazimierz', 'last_name': 'Mozil', 'points': 3426554}, {'first_name': 'Grzegorz', 'last_name': 'Strzeszewski', 'points': 1000000}, {'first_name': 'Przemek', 'last_name': 'Bieżuński', 'points': 500000}, {'first_name':
 'Przemek', 'last_name': 'Bieżuński', 'points': 445545}, {'first_name': 'Artur', 'last_name': 'Wójcik', 'points': 65432}, {'first_name': 'Grzegorz', 'last_name': 'Strzeszewski', 'points': 4324}]

place_in_the_table = 1
for player in best_scores:
    first_name = player["first_name"]
    last_name = player["last_name"]
    name = f"{first_name} {last_name}"
    print(name)
    points = player["points"]
    place_in_the_table += 1
    print(f"Miejsce {place_in_the_table}: {name:40} - {points}\n\n")