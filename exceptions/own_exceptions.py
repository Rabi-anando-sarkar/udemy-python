def brew_chai(flavor):
    if flavor not in ["masala","ginger","elaichi"]:
        raise ValueError("Unsupported chai flavour...")
    print(f"brewing {flavor} chai...")

brew_chai("masala")
brew_chai("lemon")