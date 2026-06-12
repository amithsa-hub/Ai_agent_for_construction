import pandas as pd

def generate_boq(area):

    concrete = area * 0.04
    steel = area * 4
    brickwork = area * 8

    data = {
        "Item":[
            "Concrete",
            "Steel",
            "Brickwork"
        ],
        "Quantity":[
            concrete,
            steel,
            brickwork
        ],
        "Unit":[
            "m³",
            "kg",
            "Nos"
        ]
    }

    return pd.DataFrame(data)
