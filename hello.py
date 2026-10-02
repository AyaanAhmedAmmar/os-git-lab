def greet(name="World", greeting="Hello"):
    """Print a greeting message with customizable greeting."""
    print(f"{greeting}, {name}!")


def greet_formal(name="World"):
    """Print a formal greeting."""
    greet(name, "Good day to you")


def greet_casual(name="World"):
    """Print a casual greeting."""
    greet(name, "Hey")


if __name__ == "__main__":
    greet()
    greet_formal("Ayaan")
    greet_casual("Friend")