from pytubefix import YouTube,Search
from time import sleep
import os
from flet import (
    Page,
    app,
    Text,
    Colors,
    ResponsiveRow,
    ThemeMode,
    Icons,
    Icon,
    alignment,
    Padding,
    Theme,
    CupertinoTextField,
    CupertinoAppBar,
    Container,
    IconButton,
    Column,
    Row,
    ProgressBar,
    MainAxisAlignment,
    ScrollMode,
    
)


def main(page:Page):
    page.vertical_alignment = alignment.top_center
    page.padding = Padding(top=5,right=0,bottom=2,left=0)
    page.horizontal_alignment = "center" 
    page.theme_mode= ThemeMode.LIGHT 
    page.theme = Theme(color_scheme_seed="green")
    page.bgcolor = Colors.GREEN_100
    page.scroll = True
    page.window_height = 740
    page.window_width = 410

    
    page.appbar = CupertinoAppBar(
        leading=Icon(Icons.ADOBE_OUTLINED),
        middle=Text("Aditya's Downtube App"),
        bgcolor=Colors.SURFACE,
    )

    boxh = 45
    boxw = 310
    fsize = 21
    green_color = Colors.GREEN_50

    search_box= CupertinoTextField(
        text_size= fsize,
        placeholder_text="Search Youtube Videos Here...",
        border_radius= 0,
        height=boxh,
        width=boxw,
        bgcolor=green_color,
        prefix=Icon(Icons.SEARCH),
        on_submit=lambda e:[progress(e),searchvideo(e),],

    )
    search_btn = IconButton(
        icon=Icons.SEARCH,
        width=45,
        height=45,
        bgcolor=Colors.GREEN_50,
        on_click=lambda e:[progress(e),searchvideo(e)],
    )

    search_results = Column(
        controls=[
            Container(
                content=ResponsiveRow(
                    controls=[
                        Text("Welcome to Downtube",size=19,text_align='center'),
                        Text("Here You can download any youtube video or audio to your gallery",size=18,text_align='center',italic=True),
                        Text("Author : Aditya Kumar.",size=16,text_align='center',color=Colors.BLUE_800),
                        ],
                        alignment=alignment.center,
                    ),
                    width=400,
                    height=500,
                    bgcolor=Colors.GREEN_200,
                    margin=4,
                    padding=4,
                    border_radius=6,
                    alignment=alignment.center
                    ),
        ],
        width=400,
        height=680,
        alignment=MainAxisAlignment.START,
        horizontal_alignment="center",
        scroll=ScrollMode.AUTO,

    )
    
    # output_dir = '/home/aditya/Downloads'
    output_dir = '/storage/emulated/0/Download'

    def searchvideo(e):

        search_results.controls.clear()
        search = search_box.value
        query = Search(search)

        try:
            for result in query.results:
                search_results.controls.append(
                    Container(
                        content=ResponsiveRow(
                        controls=[
                        Text(result.title,size=15),
                         Row(
                            controls=[
                                Text('Download '),
                                IconButton(
                                    Icons.VIDEO_FILE,
                                    on_click=lambda e:downvideo(e),
                                    data=str(result.video_id),
                                    ),
                                IconButton(
                                    Icons.AUDIO_FILE,
                                    on_click= lambda e:downaudio(e),
                                    data=str(result.video_id),
                                    ),
                                ]
                            )
                        ],
                        alignment=alignment.center,
                    ),
                    width=400,
                    height=200,
                    bgcolor=Colors.GREEN_200,
                    margin=6,
                    padding=4,
                    border_radius=6,
                    alignment=alignment.center
                    ),
                )
        except:
            search_results.controls.append(
                    Container(
                        content=ResponsiveRow(
                        controls=[
                        Text("Search not Found!",size=23,text_align="center"),

                        ],
                        alignment= "center",
                        vertical_alignment="center",
                    ),
                    width=400,
                    height=200,
                    bgcolor=Colors.GREEN_200,
                    margin=6,
                    padding=4,
                    border_radius=6,
                    alignment=alignment.center,
                
                    ),
                )
            

        page.update()

    def progress(e):
        pro = ProgressBar(width=400, color="amber", bgcolor="#eeeeee")
        search_results.controls.clear()
        search_results.controls.append(pro)
        page.update()
        sleep(3)
        search_results.controls.remove(pro)
        page.update()


    def downvideo(e):
        try:
            url = f'https://www.youtube.com/watch?v={e.control.data}'
            yt = YouTube(url)
            search_results.controls.clear()
            search_results.controls.append(
                Container(
                        content=ResponsiveRow(
                        controls=[
                        Text(yt.title,size=15),
                        Text(f'- {yt.author}',size=12),
                        Text("VIDEO[HD | 1080K ] Downloading...")
                        ],
                        alignment=alignment.center,
                    ),
                    width=400,
                    height=200,
                    bgcolor=Colors.GREEN_200,
                    margin=6,
                    padding=4,
                    border_radius=6,
                    alignment=alignment.center
                    ),
            )
            page.update()
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path=output_dir)
            search_results.controls.clear()
            search_results.controls.append(
                Container(
                        content=ResponsiveRow(
                        controls=[
                        Text(yt.title,size=15),
                        Text(f'- {yt.author}',size=12),
                        Text("VIDEO[HD | 1080K ] Downloading done !")
                        ],
                        alignment=alignment.center,
                    ),
                    width=400,
                    height=200,
                    bgcolor=Colors.GREEN_200,
                    margin=6,
                    padding=4,
                    border_radius=6,
                    alignment=alignment.center
                    ),
            )
            page.update()

        except:
            pass


    def downaudio(e):
        try:
            url = f'https://www.youtube.com/watch?v={e.control.data}'
            yt = YouTube(url)
            search_results.controls.clear()
            search_results.controls.append(
                Container(
                        content=ResponsiveRow(
                        controls=[
                        Text(yt.title,size=15),
                        Text(f'- {yt.author}',size=12),
                        Text("AUDIO[8D | MP3] Downloading...")
                        ],
                        alignment=alignment.center,
                    ),
                    width=400,
                    height=200,
                    bgcolor=Colors.GREEN_200,
                    margin=6,
                    padding=4,
                    border_radius=6,
                    alignment=alignment.center
                    ),
            )
            page.update()
            video = yt.streams.filter(only_audio=True).first()
            downloaded_file = video.download(output_path=output_dir)
            base, ext = os.path.splitext(downloaded_file)
            new_file = base + '.mp3'
            os.rename(downloaded_file, new_file)
            search_results.controls.clear()
            search_results.controls.append(
                Container(
                        content=ResponsiveRow(
                        controls=[
                        Text(yt.title,size=15),
                        Text(f'- {yt.author}',size=12),
                        Text("Downloading done !")
                        ],
                        alignment=alignment.center,
                    ),
                    width=400,
                    height=200,
                    bgcolor=Colors.GREEN_200,
                    margin=4,
                    padding=4,
                    border_radius=6,
                    alignment=alignment.center
                    ),
            )
            page.update()
          
        except:
            pass    



    page.add(
        
        ResponsiveRow(
            [
                search_box,
                search_btn
            ],
            alignment="center",
        ),
        Container(
            content=search_results,
            bgcolor= Colors.GREEN_50,
            width=400,
            height=680,
            border_radius=8,
            blur= 5,
            
        )
    )
    
    page.update()
app(target=main)