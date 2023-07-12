from GUI import init_main_window, init_authentication_label, init_date
from Functions import download_questions, init_sound_mixer


# Main
if __name__ == "__main__":
    # Initialization sound mixer call
    init_sound_mixer()
    # Download question into global list of all question
    download_questions()
    # Creating root
    root = init_main_window()
    # Initialization date call
    init_date(root)
    # Initialization authentication label call
    init_authentication_label(root)
    # mainloop for root
    root.mainloop()
