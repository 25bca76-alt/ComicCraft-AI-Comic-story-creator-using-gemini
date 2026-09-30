from datetime import datetime
from pathlib import Path

from fpdf import FPDF
from PIL import Image


BASE_DIR = Path(__file__).resolve().parent.parent.parent

EXPORT_DIR = BASE_DIR / "static" / "exports"

EXPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def safe_text(text: str) -> str:

    return (
        text
        .encode("latin-1", "replace")
        .decode("latin-1")
    )


def save_pdf(layout: list[dict]) -> Path:

    filename = (
        f"comic_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.pdf"
    )


    output = EXPORT_DIR / filename


    pdf = FPDF()


    pdf.set_auto_page_break(
        auto=True,
        margin=15
    )


    for panel in layout:

        pdf.add_page()


        pdf.set_font(
            "Helvetica",
            "B",
            18
        )


        pdf.multi_cell(
            0,
            10,
            safe_text(
                f"Panel {panel['panel_number']}: "
                f"{panel['title']}"
            )
        )


        pdf.ln(3)


        image_path = Path(
            panel["local_image_path"]
        )


        if image_path.exists():

            with Image.open(image_path) as image:

                width, height = image.size


            max_width = 180

            max_height = 105


            scale = min(
                max_width / width,
                max_height / height
            )


            pdf.image(
                str(image_path),
                w=width * scale,
                h=height * scale
            )


        pdf.ln(5)


        sections = [

            (
                "Scene",
                panel["scene_description"]
            ),

            (
                "Caption",
                panel.get("caption", "")
            ),

            (
                "Narration",
                panel.get("narration", "")
            )
        ]


        for label, value in sections:

            if not value:
                continue


            pdf.set_font(
                "Helvetica",
                "B",
                11
            )


            pdf.cell(
                0,
                7,
                safe_text(label)
            )


            pdf.ln(6)


            pdf.set_font(
                "Helvetica",
                "",
                10
            )


            pdf.multi_cell(
                0,
                6,
                safe_text(value)
            )


            pdf.ln(2)


    pdf.output(str(output))


    return output