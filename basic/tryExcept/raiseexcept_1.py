def main():
        while True:
            odp = input("Wybierz operacje (szyfrowanie, deszyfrowanie, wyjscie): ")
            if odp == "szyfrowanie":
                text = input("Podaj tekst malymi literami")
                if text.isupper():
                    raise Exception("nieprawdlowe tylko male litery")

            elif odp == "deszyfrowanie":
                 szyfr = input("Podaj tekst")
            elif odp == "wyjscie":
                break
            else:
                print("Bledna operacja")




if __name__ == "__main__":
    main()
