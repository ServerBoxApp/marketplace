import tools
import os


if __name__ == '__main__':
    # Verify all templates before merge them.
    if not tools.verify_all():
        exit(1)
    
    # Start generate this market place.
    tools.generate()