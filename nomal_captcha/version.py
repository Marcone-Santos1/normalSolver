import toml

# Your custom logic to determine the dynamic version
dynamic_version = "1.0.0"

# Load the original pyproject.toml
with open("../pyproject.toml", "r") as f:
    data = toml.load(f)

# Update the version field with the dynamic version
data["project"]["version"] = dynamic_version

# Write the updated pyproject.toml
with open("../pyproject.toml", "w") as f:
    toml.dump(data, f)
