"""
  Checks if a person plays banjo based on their name.

  Args:
    name: The person's name.

  Returns:
    A string indicating whether the person plays banjo.
"""
def areYouPlayingBanjo(name):
    if name.lower().startswith('r'):
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    
print(areYouPlayingBanjo('Ramses'))