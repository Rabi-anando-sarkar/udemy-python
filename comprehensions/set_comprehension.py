fav_colors = [
    "blue",
    "green",
    "red",
    "purple",
    "yellow",
    "yellow",
    "yellow",
    "orange"
]

unique_colors = {color for color in fav_colors}
print(unique_colors)

gradients = {
    "ocean_bliss": ["blue", "purple", "pink"],
    "sunset": ["orange", "red", "purple"],
    "aqua_lime": ["aqua", "teal", "lime"],
    "fire": ["yellow", "orange", "red"],
    "forest": ["green", "olive", "brown"],
    "twilight": ["purple", "blue", "black"]
}

color_mix = {invidiual_color for color_mix in gradients.values() for invidiual_color in color_mix}
print(color_mix)