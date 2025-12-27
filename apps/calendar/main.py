import eel

def main():
    eel.init('webapp')
    eel.start('index.html', cmdline_args=[
        '--window-size=400,650'
    ])

if __name__ == '__main__':
    main()