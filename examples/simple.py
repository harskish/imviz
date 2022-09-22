import imviz as viz
import sys

while True:
    if not viz.wait():
        sys.exit()
    
    viz.set_main_window_title("Simple Example")

    if viz.begin_window("Minimal Example"):
        if viz.button("Press me to print"):
            print("Button was pressed")
        viz.end_window()
    else:
        pass # window minimized