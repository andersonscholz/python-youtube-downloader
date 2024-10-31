from pytubefix import YouTube

def main():
    print( "__   __          _         _           ______                    _                  _           ")
    print( "\ \ / /         | |       | |          |  _  \                  | |                | |          ")
    print( " \ V /___  _   _| |_ _   _| |__   ___  | | | |_____      ___ __ | | ___   __ _   __| | ___ _ __ ")
    print( "  \ // _ \| | | | __| | | |  _ \ / _ \ | | | / _ \ \ /\ / / '_ \| |/ _ \ / _  | / _\ |/ _ \ '__|")
    print( "  | | (_) | |_| | |_| |_| | |_) |  __/ | |/ / (_) \ V  V /| | | | | (_) | (_| || (_| |  __/ |   ")
    print( "  \_/\___/ \__,_|\__|\__,_|_.__/ \___| |___/ \___/ \_/\_/ |_| |_|_|\___/ \__,_| \__,_|\___|_|   ")
    link = input("Insira a URL: ")
    try:
        yt = YouTube(link)
        print(
            f"\nTITULO DO VÍDEO SELECIONADO: \n {yt.title}\n\n"
            f"DATA DE PUBLICAÇÃO: \n {yt.publish_date}\n\n"
            f"VISUALIZAÇÕES: \n {yt.views}\n\n"
        )
        video = yt.streams.get_highest_resolution()
        video.download()
        print("Vídeo baixado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
