# Modules import.
# GUI module to initialize the graphics in the project.
from GUI import init_main_window, init_authentication_label, init_date
# Functions module for support GUI module.
from Functions import download_questions, init_sound_mixer, load_images


# Main.
if __name__ == "__main__":
    # Initialization sound mixer call.
    init_sound_mixer()
    # Download question into global list of all question.
    download_questions()
    # Creating root
    root = init_main_window()
    # Loading images to global dictionary.
    load_images()
    # Initialization date call.
    init_date(root)
    # Initialization authentication label call.
    init_authentication_label(root)
    # mainloop for root.
    root.mainloop()
