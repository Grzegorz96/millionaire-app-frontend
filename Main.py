from GUI import init_main_window, init_authentication_label, init_date
from Functions import download_questions
    # playsound(r"C:\Users\grzes\Desktop\Projekty Python\Milionarie.app\Frontend\start_music.mp3")



if __name__ == "__main__":
    root = init_main_window()
    download_questions()
    init_date(root)
    init_authentication_label(root)


    root.mainloop()