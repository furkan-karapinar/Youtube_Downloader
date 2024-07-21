from pytube import YouTube


class youtubedownlaoder:
    def __init__(self,url):
        self.url = url
        self.yt = YouTube(url)
    def get_video_info(self):
        return {
            'title': self.yt.title,
            'lenght': self.yt.length,
            'description': self.yt.description,
            'views': self.yt.views,
        }
    def download(self,quality='highest'):
        if quality == 'highest':
            video_stream = self.yt.streams.get_highest_resolution()
        elif quality == 'lower':
            video_stream = self.yt.streams.get_lowest_resolution()
        else:
            raise ValueError("Unknown ResolutionType Error")
        print(f"---> {self.yt.title} İndiriliyor...")
        video_stream.download()
        print("---> İndirme Tamamlandı!")

if __name__ == '__main__':
    url = input("Youtube linkini yazınız: ")
    downloader = youtubedownlaoder(url)
    print("\n---------------------------------------\n")
    info = downloader.get_video_info()
    print(f"Video Info:\n Title: {info['title']}\nLenght: {info['lenght']} seconds\nDescription {info['description']}\nViews {info['views']}")
    downloader.download()
