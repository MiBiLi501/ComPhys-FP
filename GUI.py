import tkinter as tk

import Shape

from Environment import Environment

def reset_env_prompt(env: Environment):
    def success():
        env.dynamicObjects = list()
        confirmation.destroy()

    confirmation = tk.Tk()
    confirmation.title("Reset confirmation")
    tk.Label(confirmation, text="Are you sure you want to reset the environment?").pack()

    tk.Button(confirmation, text="confirm", command=lambda: success()).pack()
    confirmation.mainloop()
    print("reset")


def add_shape_prompt(env: Environment):
    add_shape = tk.Tk()
    add_shape.title("Add Shape")
    # add_shape.geometry("300x400")
    tk.Label(add_shape, text="Select Shape").pack()

    shape_var = tk.StringVar()

    tk.Radiobutton(add_shape, text="Rectangle", variable=shape_var, value="rectangle").pack(anchor='w')
    tk.Radiobutton(add_shape, text="Triangle", variable=shape_var, value="triangle").pack(anchor='w')

    tk.Button(add_shape, text="Choose shape", command=lambda: add_shape.destroy() if shape_var.get() else None).pack()

    add_shape.mainloop()

    match shape_var.get():
        case "triangle":

            def validate():
                try:
                    originx = float(originx_var.get("1.0", "end-1c"))
                    originy = float(originy_var.get("1.0", "end-1c"))
                    length = int(length_var.get("1.0", "end-1c"))
                    gap = float(gap_var.get("1.0", "end-1c"))
                    stiffness = float(stiffness_var.get("1.0", "end-1c"))
                    dampiness = float(dampiness_var.get("1.0", "end-1c"))

                except:
                    return False

                new_shape = Shape.ReinforcedTriangle(origin=(originx, originy), length=length, gap=gap, stiffness=stiffness, damping=dampiness)

                env.add_dynamic_body(new_shape)

                return True


            properties = tk.Tk()
            properties.title("Set properties")
            tk.Label(properties, text="origin x").grid(column=0, row=0)
            originx_var = tk.Text(properties, height=1, width=5)
            originx_var.grid(column=0, row=1)
            tk.Label(properties, text="origin y").grid(column=1, row=0)
            originy_var = tk.Text(properties, height=1, width=5)
            originy_var.grid(column=1, row=1)
            tk.Label(properties, text="length").grid(column=2, row=0)
            length_var = tk.Text(properties, height=1, width=5)
            length_var.grid(column=2, row=1)
            tk.Label(properties, text="gap").grid(column=3, row=0)
            gap_var = tk.Text(properties, height=1, width=5)
            gap_var.grid(column=3, row=1)
            tk.Label(properties, text="stiffness").grid(column=1, row=2)
            stiffness_var = tk.Text(properties, height=1, width=5)
            stiffness_var.grid(column=1, row=3)
            tk.Label(properties, text="damping").grid(column=2, row=2)
            dampiness_var = tk.Text(properties, height=1, width=5)
            dampiness_var.grid(column=2, row=3)

            tk.Button(properties, text="Confirm", command=lambda: properties.destroy() if validate() else None).grid(column=0, row=5)

            properties.mainloop()

        case "rectangle":

            def validate():
                try:
                    originx = float(originx_var.get("1.0", "end-1c"))
                    originy = float(originy_var.get("1.0", "end-1c"))
                    width = int(width_var.get("1.0", "end-1c"))
                    height = int(height_var.get("1.0", "end-1c"))
                    gap = float(gap_var.get("1.0", "end-1c"))
                    stiffness = float(stiffness_var.get("1.0", "end-1c"))
                    dampiness = float(dampiness_var.get("1.0", "end-1c"))

                except:
                    return False

                new_shape = Shape.ReinforcedRectangle(origin=(originx, originy), width=width, height=height, gap=gap, stiffness=stiffness, damping=dampiness)

                env.add_dynamic_body(new_shape)

                return True


            properties = tk.Tk()
            properties.title("Set properties")
            tk.Label(properties, text="origin x").grid(column=0, row=0)
            originx_var = tk.Text(properties, height=1, width=5)
            originx_var.grid(column=0, row=1)
            tk.Label(properties, text="origin y").grid(column=1, row=0)
            originy_var = tk.Text(properties, height=1, width=5)
            originy_var.grid(column=1, row=1)
            tk.Label(properties, text="width").grid(column=2, row=0)
            width_var = tk.Text(properties, height=1, width=5)
            width_var.grid(column=2, row=1)
            tk.Label(properties, text="length").grid(column=3, row=0)
            height_var = tk.Text(properties, height=1, width=5)
            height_var.grid(column=3, row=1)
            tk.Label(properties, text="gap").grid(column=4, row=0)
            gap_var = tk.Text(properties, height=1, width=5)
            gap_var.grid(column=4, row=1)
            tk.Label(properties, text="stiffness").grid(column=1, row=2)
            stiffness_var = tk.Text(properties, height=1, width=5)
            stiffness_var.grid(column=1, row=3)
            tk.Label(properties, text="damping").grid(column=3, row=2)
            dampiness_var = tk.Text(properties, height=1, width=5)
            dampiness_var.grid(column=3, row=3)

            tk.Button(properties, text="Confirm", command=lambda: properties.destroy() if validate() else None).grid(column=0, row=5)

            properties.mainloop()