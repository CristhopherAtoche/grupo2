import time
import assets

def main():
    print("INICIANDO....")
    while True:
        result = assets.access()
        if len(result) == 2 and result[0] == 1:
            assets.save()
            assets.update_gate_status(result[1], 0)
        time.sleep(2)
        print("------------------------------------------------")

if __name__ == '__main__':
    main()
