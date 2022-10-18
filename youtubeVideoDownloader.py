import getpass
import os
import pytube
import dearpygui.dearpygui as dpg


pref_list = ["mp4", "mp3", "Any"]
def down():
    comp_name = getpass.getuser() #get the computer's name
    Save_Path = "C:/Users/"+comp_name+"/Downloads"
    print(dpg.get_value("pref"))
    try:
        yt = pytube.YouTube(dpg.get_value("link"))
        print(yt.title + " is downloading . . . ")
        if dpg.get_value("pref") == "mp3":
            stream = yt.streams.filter(only_audio=True).first()
            out_file = stream.download(r'%s' %Save_Path)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
        else:
            stream = yt.streams.get_highest_resolution()
            stream.download(r'%s' %Save_Path)
        print("Done!!!")
        dpg.destroy_context()
    except:
        
        print("Error")


dpg.create_context()


with dpg.window(tag="Youtube Download"):
    dpg.add_text("Please Input the link")
    dpg.add_input_text(tag="link")
    dpg.add_text("Your Preference: ")
    dpg.add_listbox(items=pref_list, tag="pref")
    dpg.add_button(label="Download", callback=down)
    
dpg.create_viewport(title="Video Downloader", width=520, height=600)
dpg.setup_dearpygui()
dpg.set_primary_window("Youtube Download", True)
dpg.show_viewport()
dpg.start_dearpygui()