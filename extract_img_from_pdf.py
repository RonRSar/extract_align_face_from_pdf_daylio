#Libraries
import fitz
import os


#change file name
daylio_file ="\daylio_export_2025_03_06.pdf"

def extract_img_from_pdf(daylio_file):
    #extraction
    rawpath = str(os.getcwd())
    filepath = rawpath + daylio_file
    imagepath = rawpath + "\image.png"

    pdf_file = fitz.open(filepath)
    count = 0

    for page_index in range(len(pdf_file)):
        page = pdf_file[page_index]
        image_list = page.get_images()

        if image_list:
            print(
                f"[+] Found a total of {len(image_list)} images in page {page_index}"
            )
        else:
            print("no images")

        for image_index in range(len(image_list)):
            if (image_list[image_index][3]) > 250:
                img = pdf_file.extract_image(image_list[image_index][0])
                with open(f"image.{img['ext']}", "wb") as imgout:
                    imgout.write(img["image"])

                pic_dex = str(count)
                count += 1
                newimgpath = rawpath + "\daylio_image_" + pic_dex + ".jpeg"
                os.rename(imagepath, newimgpath)

if __name__ == '__main__':
    extract_img_from_pdf(daylio_file)


      



