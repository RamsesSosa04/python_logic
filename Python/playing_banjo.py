def areYouPlayingBanjo(name):
    if name.lower().startswith('r'):
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    
print(areYouPlayingBanjo('Ramses'))