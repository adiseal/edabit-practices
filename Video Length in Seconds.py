def minutes_to_seconds(video_length: str) -> int:
    minutes, seconds = map(int, video_length.split(':'))
    if seconds >= 60:
        return False
    return minutes * 60 + seconds

print(minutes_to_seconds("01:00")) # 60
print(minutes_to_seconds("13:56")) # 836
print(minutes_to_seconds("10:60")) # False