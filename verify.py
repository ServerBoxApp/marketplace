import tools
if __name__ == '__main__':
    if tools.verify_all():
        print("All templates has been verified.")
    else:
        print("Error happend during verify.")