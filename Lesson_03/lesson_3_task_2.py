from smartphone import Smartphone

catalog = [
    Smartphone("Siemens", "A35", "+71234567890"),
    Smartphone("Sony", "M100", "+76783268391"),
    Smartphone("Motorola", "E250", "+79107539823"),
    Smartphone("Samsung", "FZ666", "+79068395682"),
    Smartphone("Meizu", "G910", "+79511239847")
]

for smartphone in catalog:

    print(f"{smartphone._marka} - {smartphone._model}. {smartphone._number}")
