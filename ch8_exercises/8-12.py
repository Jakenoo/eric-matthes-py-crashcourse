def make_sandwich(*works):
    """Prints all specifications for sandwich"""
    print("You ordered a sandwich with:")
    for order in works:
        print(f"- {order}")

make_sandwich('shmear of poop', 'poop on the side', 'skidmark')
make_sandwich('poop')
make_sandwich("pipin' port-a-john")