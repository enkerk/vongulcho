"""A traditional roguelike"""
import tcod.context
import tcod.tileset

def main():
    """The main function (the fuck am I supposed to put here)"""
    tileset = tcod.tileset.load_tilesheet(
        "vg/data/Alloy_curses_12x12.png", columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437
    )
    tcod.tileset.procedural_block_elements(tileset=tileset)
    console = tcod.console.Console(80, 50)
    console.print(0, 0, "Hello World!")
    with tcod.context.new(tileset=tileset) as context:
        while True: # Main loop
            context.present(console) # Render the console to the window
            for event in tcod.event.wait(): # Event Loop, blocks until pending events exist
                print(event)
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()

if __name__ == "__main__":
    main()
