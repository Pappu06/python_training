# Dictionary in python

player = {
    "name": "Dhoni",
    "age": 41,
    "city": "Rachi"
}
print(player)  # Print the dictionary

# Accessing values in a dictionary
print(player["name"])  # Print the value associated with the key "name"
print(player["age"])   # Print the value associated with the key "age"
print(player["city"])  # Print the value associated with the key "city"

# Adding new key-value pairs to a dictionary
player["team"] = "India"  # Add a new key-value pair to the dictionary
print(player)  # Print the updated dictionary

# Updating values in a dictionary
player["age"] = 42  # Update the value associated with the key "age"
print(player)  # Print the updated dictionary

# Deleting key-value pairs from a dictionary
del player["city"]  # Delete the key-value pair with the key "city"
print(player)  # Print the updated dictionary after deletion

# Dictionary methods
# keys() method
print(player.keys())  # Print all the keys in the dictionary

# values() method
print(player.values())  # Print all the values in the dictionary

# items() method
print(player.items())  # Print all the key-value pairs in the dictionary

# get() method
print(player.get("name"))  # Get the value associated with the key "name"
print(player.get("age"))   # Get the value associated with the key "age"

# remove() method
player.pop("team")  # Remove the key-value pair with the key "team"
print(player)  # Print the updated dictionary after removing the key-value pair
