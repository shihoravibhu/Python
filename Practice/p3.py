def div(a,b):
    try:
        c = a // b
    except Exception as msg:
        print(msg)
    else:
        print("Division successfully Done")
        return c
    finally:
        print("End Of The Code.")

print(div(4,0))