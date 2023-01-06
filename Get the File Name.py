def get_filename(path):
    file_name = path.split("/")
    return file_name[-1]



assert get_filename("C:/Projects/pil_tests/ascii/edabit.txt") == "edabit.txt"

assert get_filename("C:/Users/johnsmith/Music/Beethoven_5.mp3") == "Beethoven_5.mp3"

assert get_filename("ffprobe.exe") == "ffprobe.exe"