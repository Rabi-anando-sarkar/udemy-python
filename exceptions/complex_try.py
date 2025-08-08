def serve_chai(flavour):
    try:
        print(f"Preparing {flavour} chai...")
        if flavour == "unknown":
            raise ValueError("We dont know that flavour")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavour} chai is served")
    finally: 
        print("Next customer please")

serve_chai("masala")
serve_chai("unknown")