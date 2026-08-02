def main():
    try:
        a=int(input("Hay,Enter a number:"))
        print(a)

    except Exception as e:
        print(e)

    finally:
        print("Thank You.....")

main()

#finally function always run,It does not metter that the function is called or not......