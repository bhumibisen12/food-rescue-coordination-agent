"""Export PowerPoint presentation slides to PNG images using win32com."""

import os
import win32com.client

def export_slides():
    ppt_path = os.path.abspath("Surplus_Router_AI_Solutions_Presentation.pptx")
    out_dir = os.path.abspath("presentation_slides_preview")
    os.makedirs(out_dir, exist_ok=True)

    powerpoint = win32com.client.Dispatch("PowerPoint.Application")
    # Open presentation in read-only and without displaying window
    deck = powerpoint.Presentations.Open(ppt_path, WithWindow=False)

    for i, slide in enumerate(deck.Slides):
        slide_img = os.path.join(out_dir, f"slide_{i+1:02d}.png")
        slide.Export(slide_img, "PNG", 1920, 1080)
        print(f"Exported Slide {i+1} -> {slide_img}")

    deck.Close()
    powerpoint.Quit()
    print("All slides exported successfully!")

if __name__ == "__main__":
    export_slides()
