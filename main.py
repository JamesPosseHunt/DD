import dearpygui.dearpygui as dpg
from dice import roll_die

def exit_app():
    dpg.stop_dearpygui()

def dice_btn(sides):
    result = roll_die(int(sides))
    dpg.set_value("result_text", f"You rolled a {result}!")
    dpg.show_item("result_window")

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.window(label="DD", width=1920, height=1080):
    with dpg.menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="New Game")
            dpg.add_menu_item(label="Load Game")
            dpg.add_menu_item(label="Save Game")
            dpg.add_menu_item(label="Exit", callback=exit_app)

    dpg.add_text("Welcome to DD!")

    with dpg.child_window(label="Dice Roller", width=50, height=160):
        dpg.add_button(label="D4", callback=lambda: dice_btn(4))
        dpg.add_button(label="D6", callback=lambda: dice_btn(6))
        dpg.add_button(label="D8", callback=lambda: dice_btn(8))
        dpg.add_button(label="D10", callback=lambda: dice_btn(10))
        dpg.add_button(label="D12", callback=lambda: dice_btn(12))
        dpg.add_button(label="D20", callback=lambda: dice_btn(20))

    with dpg.child_window(label="Result", width=300, height=300, tag="result_window", show=False):
        dpg.add_text(default_value="", tag="result_text")
        dpg.add_button(label="Okay", callback=lambda: dpg.hide_item("result_window"))

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
