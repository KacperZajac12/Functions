import converters

def main():
    # podstawowe testy
    print("100 cm to m:", converters.cm_to_m(100))
    print("2 m to cm:", converters.m_to_cm(2))

    # nowe funkcje
    print("50 cm to inches:", converters.cm_to_inches(50))

    # feet + inches → cm
    f = 5
    inch = 7
    print(f"{f} feet {inch} inches to cm:", converters.feet_inches_to_cm(f, inch))


if __name__ == "__main__":
    main()
