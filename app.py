import tkinter as tk
from PIL import Image, ImageTk
import sys
import os

def main():
    root = tk.Tk()
    
    # Ẩn thanh tiêu đề và viền cửa sổ
    root.overrideredirect(True)
    
    # Luôn hiển thị trên cùng
    root.attributes('-topmost', True)
    
    # Chọn một màu đặc biệt làm màu trong suốt (Windows sẽ ẩn màu này đi)
    # Dùng màu không có trong hình ảnh (VD: xanh chuối)
    transparent_color = '#00ff00' 
    root.config(bg=transparent_color)
    root.attributes('-transparentcolor', transparent_color)
    
    try:
        # Load hình ảnh đã tách nền
        # Đảm bảo file 'hinh_anh.png' nằm cùng thư mục với file chạy
        img = Image.open("hinh_anh.png")
        photo = ImageTk.PhotoImage(img)
        
        # Hiển thị ảnh trên một Label có màu nền trùng với màu trong suốt
        label = tk.Label(root, image=photo, bg=transparent_color)
        label.pack()
        
        # --- THÊM TÍNH NĂNG KÉO THẢ VÀ TẮT ---
        # Nhấn ESC để thoát chương trình
        root.bind('<Escape>', lambda e: root.destroy())
        
        # Code cho phép dùng chuột kéo hình ảnh đi nơi khác
        def start_move(event):
            root.x = event.x
            root.y = event.y

        def do_move(event):
            deltax = event.x - root.x
            deltay = event.y - root.y
            x = root.winfo_x() + deltax
            y = root.winfo_y() + deltay
            root.geometry(f"+{x}+{y}")

        label.bind("<ButtonPress-1>", start_move)
        label.bind("<B1-Motion>", do_move)
        
    except Exception as e:
        print("Không tìm thấy file hinh_anh.png. Nhấn ESC để thoát.")
        root.bind('<Escape>', lambda e: root.destroy())

    root.mainloop()

if __name__ == "__main__":
    main()