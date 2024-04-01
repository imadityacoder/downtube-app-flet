from pytube import YouTube,Playlist
from flet import (
    Page,
    app,
    Text,
    TextField,
    colors,
    Row,
    ThemeMode,
    icons,
    Icon,
    AppView,
    AppBar,
    ElevatedButton,
    alignment,
    Padding,
    Theme
)


def main(page:Page):
    page.title="Welcome to Aditya's Youtube-Video-Downloader"
    page.vertical_alignment = alignment.top_center
    page.padding = Padding(top=100,right=0,bottom=0,left=0)
    page.horizontal_alignment = "center" 
    page.theme_mode= ThemeMode.LIGHT 
    page.theme = Theme(color_scheme_seed="pink")  
    page.bgcolor = colors.PINK_100
    page.scroll = True
    
    page.appbar = AppBar(
        leading=Icon(icons.APPS_OUTAGE_SHARP),
        leading_width=30,
        title=Text("Aditya's Downtube App"),
        center_title=False,
        bgcolor=colors.SURFACE_VARIANT,
    )

    boxh = 80
    boxw = 600
    fsize = 16

    urltext = Text(
        value="Enter your URL here:",
        size=17,

        )
    
    page.update()    

    urlbox= TextField(
        text_size= fsize,
        border_radius= 8,
        height=boxh,
        width=boxw,
        opacity=0.9,
        bgcolor=colors.PURPLE_50,
        border_color="black",
        hint_text="https://www.youtube.com/watch?v=Vds8ddYXYZY"
    )
    output_dir = '/home/aditya/Downloads/'
    def downvideo(e):
        yt = YouTube(str(urlbox.value))
        page.add(Text(value=yt.title+" downloading..."))
        page.update()
        stream = yt.streams.get_highest_resolution()
        page.add(Text(value=yt.title+" download in few minutes"))
        stream.download(output_path=output_dir)
        page.add(Text(value=yt.title+" downloading done!"))
        page.update()
        

    def downplaylist(e):
        p = Playlist(str(urlbox.value))

        p_len=len(p)
        no = 1

        page.add(Text(f"Total number of videos in this playlist is {p_len}"))
        for url in p.video_urls[:p_len]:
            link = str(url)
            page.add(Text(f'Downloading video {no} : {link.title}...') )
            no += 1             
            yt = YouTube(link)
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path=output_dir)
            page.add(Text(f'Downloading video {no} : {link.title} done!') )
            page.update() 

    def download(e):
        try:    
            if "playlist" in urlbox.value:
                downplaylist(e)
            else:
                downvideo(e)
        except:
            page.add(Text(f"Sorry! I can't found this '{urlbox.value}' url or\n       You entered the wrong url!"))        

    btndown= ElevatedButton(
        text="download now",
        icon=icons.DOWNLOADING_ROUNDED,
        opacity=0.8,
        width=boxw-100,
        height=boxh-40,
        on_click=lambda e:download(e),
        )


    page.add(
        Row(
            [
                urltext,  
            ],
            alignment="center",
        ),
        Row(
            [
                urlbox,
            ],
            alignment="center",
        ),
        Row(
            [
                btndown,
            ],
            alignment="center",
        ),

    )
    
    page.update()

if __name__=="__main__":

    app(target=main)
