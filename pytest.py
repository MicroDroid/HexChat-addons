"""
This script tests the addons.

You ***SHOULDN'T*** load this on your HexChat. :)
"""

if __name__ == "__main__":
    import os
    import sys
    broken = 0
    print("HexChat addons test script.")
    print("There might been shown weird stuff. Don't worry. :)\n")
    for val in os.listdir("addons"):
        print("Testing {0}".format(val))
        try:
            __import__('addons.{0}'.format(val.replace(".py", "")), globals={"__name__": __name__})
            print("{0} is WORKING.".format(val))
        except Exception as err:
            print("{0} is FAILING. ({1})".format(val, err))
            broken = 1
    if broken == 1:
        print("\nThere's broken addons. :(")
        sys.exit(1)
    else:
        print("\nAll is fine. :)")
        sys.exit(0)
