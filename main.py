import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.window(label="DD"):
    dpg.add_text("Welcome to DD.")


dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()